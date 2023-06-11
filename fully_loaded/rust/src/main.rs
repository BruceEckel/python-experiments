use std::sync::{Arc, Mutex};
use std::time::Instant;

fn cpu_intensive(n: u128, multiplier: u8) -> f64 {
    let mut result: f64 = 0.0;
    for i in 0..(10u128.pow(7) * multiplier as u128) {
        result += ((i.pow(3) + i.pow(2) + i * n) as f64).sqrt() as f64;
    }
    result
}

#[tokio::main]
async fn main() {
    let multiplier: u8 = 1; // Increase for longer computations
    let logical_processors = num_cpus::get();
    dbg!(logical_processors);
    let tasks = (logical_processors - 0) * 1; // Try different numbers
    dbg!(tasks);
    let start = Instant::now();

    let results = Arc::new(Mutex::new(Vec::new()));
    let mut handles = Vec::new();

    for i in 0..tasks {
        let results = Arc::clone(&results);
        handles.push(tokio::spawn(async move {
            let result = cpu_intensive(i as u128, multiplier);
            let mut results = results.lock().unwrap();
            results.push(result);
        }));
    }

    for handle in handles {
        handle.await.unwrap();
    }

    let results = Arc::try_unwrap(results).unwrap().into_inner().unwrap();
    println!("{:?}", results);
    println!("Elapsed time: {:.2}s", start.elapsed().as_secs_f64());
}
