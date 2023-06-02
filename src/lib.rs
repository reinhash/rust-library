use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn big_calculation(elements: usize) {
    let mut big_array = vec![0; elements];
    for i in 0..elements {
        big_array[i] = i;
    }
    return;
}

/// A Python module implemented in Rust.
#[pymodule]
fn rust_library(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(big_calculation, m)?)?;
    Ok(())
}