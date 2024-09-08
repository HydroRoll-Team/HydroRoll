from oneroll import roll


class Cli:
    def parser():
        while True:
            try:
                roll_result = roll(input(), allow_comments=True)
                print(
                    f"""==============
{roll_result},
<ast: {roll_result.ast}>,
<crit: {roll_result.crit}>,
<comment: {roll_result.comment}>
{roll_result.expr}
==============""".strip()
                )
            except Exception as e:
                print(e)
