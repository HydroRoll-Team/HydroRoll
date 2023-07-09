import Image from "next/image";
import type { AuthorDetails } from "../content/team";

export const Avatar = ({ name, picture, twitterUsername }: AuthorDetails) => (
  <div className="flex items-center flex-shrink-0 md:justify-start">
    <div className="w-[32px] h-[32px]">
      <Image
        src={picture}
        height={32}
        width={32}
        title={name}
        className="w-full rounded-full"
        alt={name}
        priority
      />
    </div>
    <dl className="ml-2 text-sm font-medium leading-4 text-left whitespace-no-wrap">
      <dt className="sr-only">Name</dt>
      <dd className="text-gray-900 dark:text-white">{name}</dd>
      {GithubUsername && (
        <>
          <dt className="sr-only">Github</dt>
          <dd>
            <a
              href={`https://github.com/${GithubUsername}`}
              className="text-xs text-blue-500 no-underline betterhover:hover:text-blue-600 betterhover:hover:underline"
              target="_blank"
              rel="noopener noreferrer"
            >
              {`@${GithubUsername}`}
            </a>
          </dd>
        </>
      )}
    </dl>
  </div>
);
