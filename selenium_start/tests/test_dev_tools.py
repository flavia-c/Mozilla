from selenium_start.pages.dev_tools import DevTools

def test_dev_tools(selenium, variables):
    tools = DevTools(selenium, variables, open_url=True)
    assert tools.core_tools_button_is_enabled()



