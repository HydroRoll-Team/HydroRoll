try:
    import lupa.luajit2 as lupa
except ImportError:
    try:
        import lupa.lua54 as lupa
    except ImportError:
        try:
            import lupa.lua53 as lupa
        except ImportError:
            import lupa

print(
    f"Using {lupa.LuaRuntime().lua_implementation} (compiled with {lupa.LUA_VERSION})"
)

from lupa import LuaRuntime

lua = LuaRuntime(unpack_returned_tuples=True)
import os


def get_Dice_Dir():
    return os.path.dirname(os.path.abspath("__file__"))


lua.globals().getDiceDir = get_Dice_Dir
lua.globals().package.path = (
    lua.globals().package.path
    + ";"
    + os.path.join(get_Dice_Dir(), "?.lua")
    + ";"
    + os.path.join(get_Dice_Dir(), "?.dll")
    + ";"
    + os.path.join(os.path.dirname(os.path.abspath(__file__)), "?.lua")
    + ";"
    + os.path.join(os.path.dirname(os.path.abspath(__file__)), "?.dll")
)

try:
    lua.execute(
        """\
    print()
    print(getDiceDir())
    print()
    print(package.path)
    js = require('json')
    print()
    print(js)
            """
    )
except Exception as e:
    print(f"{e!r}")
