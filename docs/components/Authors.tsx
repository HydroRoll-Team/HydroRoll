import { Avatar } from "./Avatar";
import cn from "classnames";
import HYDROROLL_TEAM from "../content/team";
import type { Author } from "../content/team";

export function Authors({ authors }: { authors: Array<Author> }) {
  const validAuthors = authors.filter((author) => HYDROROLL_TEAM[author]);
  return (
    <div className="w-full border-b border-gray-400 authors border-opacity-20">
      <div
        className={cn(
          "flex flex-wrap justify-center py-8 mx-auto gap-7",
          authors.length > 4 && "max-w-3xl"
        )}
      >
        {validAuthors.map((username) => (
          <Avatar key={username} {...HYDROROLL_TEAM[username]} />
        ))}
      </div>
    </div>
  );
}
