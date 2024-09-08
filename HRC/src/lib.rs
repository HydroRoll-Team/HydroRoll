use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn process_rule_pack(rule_pack: &str) -> PyResult<String> {
    Ok(format!("Processed rule pack: {}", rule_pack))
}

#[pymodule]
#[pyo3(name = "LibCore")]
fn libcore(_py: Python, m: &PyModule) -> PyResult<()> {
    let _py_hrc_log = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/hrc/log.py"));
    let _py_hrc_event = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/hrc/event.py"));
    let _py_hrc_core = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/hrc/core.py"));
    let _py_hrc_const = include_str!(concat!(env!("CARGO_MANIFEST_DIR"), "/hrc/const.py"));

    m.add_function(wrap_pyfunction!(process_rule_pack, m)?)?;
    Ok(())
}
