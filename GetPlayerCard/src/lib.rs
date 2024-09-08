use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn process_rule_pack(rule_pack: &str) -> PyResult<String> {
    Ok(format!("Processed rule pack: {}", rule_pack))
}

#[pymodule]
#[pyo3(name = "LibCore")]
fn libcore(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(process_rule_pack, m)?)?;
    Ok(())
}