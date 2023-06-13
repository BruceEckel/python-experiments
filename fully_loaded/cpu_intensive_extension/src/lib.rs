use pyo3::prelude::*;
// use pyo3::types::IntoPyDict;

#[pymodule]
fn cpu_intensive_extension(py: Python, m: &PyModule) -> PyResult<()> {
    #[pyfunction]
    fn cpu_intensive_py(n: u64, multiplier: u8) -> f64 {
        let mut result: f64 = 0.0;
        for i in 0..(10u64.pow(7) * multiplier as u64) {
            result += ((i.pow(3) + i.pow(2) + i * n) as f64).sqrt();
        }
        result
    }

    m.add_function(wrap_pyfunction!(cpu_intensive_py, m)?)?;

    Ok(())
}

#[pymodule]
fn cpu_intensive_extension_py(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_submodule(cpu_intensive_extension(py, m)?)?;

    Ok(())
}

#[pymodule]
fn cpu_intensive_extension_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(cpu_intensive_extension_py, m)?)?;

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use pyo3::types::IntoPyDict;
    use pyo3::types::IntoPyTuple;
    use pyo3::types::PyTuple;

    #[test]
    fn test_cpu_intensive() {
        let gil = Python::acquire_gil();
        let py = gil.python();

        let m = PyModule::new(py, "test_module").unwrap();
        cpu_intensive_extension_py(py, &m).unwrap();
        let locals = [("test_module", m)].into_py_dict(py);

        let result: f64 = py
            .eval(
                "result = test_module.cpu_intensive(10, 1)\nresult",
                Some(locals),
                None,
            )
            .unwrap()
            .extract()
            .unwrap();

        assert!(result > 0.0);
    }
}
