use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn big_calculation() -> Py<PyAny> {
    let mut big_array = vec![0; 1_000_000];
    for i in 0..1_000_000 {
        big_array[i] = i;
    }
    return Python::with_gil(|py| {
        big_array.to_object(py)
    });
}

/// A Python module implemented in Rust.
#[pymodule]
fn rust_library(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(big_calculation, m)?)?;
    Ok(())
}