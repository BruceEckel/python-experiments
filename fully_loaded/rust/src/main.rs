use tokio::sync::mpsc;
use std::time::Instant;

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
    let timer = Instant::now();

    let (tx, mut rx) = mpsc::channel(tasks);

    for i in 0..tasks {
        let tx = tx.clone();
        tokio::spawn(async move {
            let result = cpu_intensive(i as u128, multiplier);
            tx.send(result).await.unwrap();
        });
    }

    drop(tx); // Drop the transmitter to close the channel

    while let Some(result) = rx.recv().await {
        println!("{:?}", result);
    }

    println!("Elapsed time: {:.2}s", timer.elapsed().as_secs_f64());
}
