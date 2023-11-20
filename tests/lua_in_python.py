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
    return os.path.dirname(os.path.abspath(__file__))


lua.globals().getDiceDir = get_Dice_Dir
lua.globals().package.path = lua.globals().package.path + ';' + os.path.join(get_Dice_Dir(), '?.lua')
try:
    lua.execute(
        """\
    print(getDiceDir())
    print(package.path)
    js = require('json')
    print(js)
            """ 
    )
except Exception as e:
    print(f'{e!r}')