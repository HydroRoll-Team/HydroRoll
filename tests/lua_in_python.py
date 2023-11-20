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

print(f"Using {lupa.LuaRuntime().lua_implementation} (compiled with {lupa.LUA_VERSION})")