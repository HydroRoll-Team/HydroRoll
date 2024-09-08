from infini.input import Input


def test_new_input_without_vars():
    assert Input("test plain_str").plain_data == "test plain_str"
    assert Input("test plain_str").get_plain_text() == "test plain_str"


def test_new_input_with_session_id():
    input = Input("test plain_str", variables={"session_id": "test"})
    assert input.get_session_id() == "test"


def test_new_input_without_session_id():
    input = Input("test plain_str", variables={"user_id": "test"})
    assert input.get_session_id() == "test"
