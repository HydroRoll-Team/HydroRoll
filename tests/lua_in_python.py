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
import asyncio

async def get_Dice_Dir():
    import os
    await asyncio.sleep(1)
    return os.path.dirname(os.path.abspath(__file__))


lua.globals().getDiceDir = get_Dice_Dir

print(
    lua.eval(
        """\
    getDiceDir()
               """
    )
)
