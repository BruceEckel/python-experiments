use std::sync::{Arc, Mutex};
use std::time::Instant;
use tokio::sync::mpsc;

fn cpu_intensive(n: u128, multiplier: u8) -> f64 {
    let mut result: f64 = 0.0;
    for i in 0..(10u128.pow(7) * multiplier as u128) {
        result += ((i.pow(3) + i.pow(2) + i * n) as f64).sqrt();
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

    let (tx, mut rx) = mpsc::channel(tasks);

    for i in 0..tasks {
        let tx = tx.clone();
        tokio::spawn(async move {
            let result = cpu_intensive(i as u128, multiplier);
            tx.send(result).await.unwrap();
        });
    }

    drop(tx); // Drop the transmitter to close the channel

    let results = Arc::new(Mutex::new(Vec::new()));
    while let Some(result) = rx.recv().await {
        let mut results = results.lock().unwrap();
        results.push(result);
    }

    let results = Arc::try_unwrap(results).unwrap().into_inner().unwrap();
    println!("{:?}", results);
    println!("Elapsed time: {:.2}s", start.elapsed().as_secs_f64());
}
