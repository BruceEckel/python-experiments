use pyo3::prelude::*;

#[pyfunction]
fn cpu_intensive(n: u128, multiplier: u128) -> PyResult<f64> {
    let mut result: f64 = 0.0;
    for i in 0..(10_000_000 * multiplier) {
        result += ((i.pow(3) + i.pow(2) + i * n) as f64).sqrt();
    }
    Ok(result)
}

#[pymodule]
fn rust_extension(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(cpu_intensive, m)?)?;
    Ok(())
}
