import cn from "classnames";
import { useRouter } from "next/router";
import Link from "next/link";

export type TurboSite = "TRPG" | "AI";

export function useTurboSite(): TurboSite | undefined {
  const { pathname } = useRouter();

  if (pathname.startsWith("/AI")) {
    return "AI";
  }

  if (pathname.startsWith("/TRPG")) {
    return "TRPG";
  }

  return undefined;
}

function SiteSwitcherLink({ href, text, isActive }) {
  const classes =
    "py-1 transition-colors duration-300 inline-block w-[50px] cursor-pointer hover:text-black dark:hover:text-white";

  const conditionalClasses = {
    "text-black dark:text-white": !!isActive,
  };

  return (
    <Link href={href} className={cn(classes, conditionalClasses)}>
      {text}
    </Link>
  );
}

function SiteSwitcher() {
  const site = useTurboSite();

  return (
    <div className="relative flex items-center justify-between p-2 text-xl group">
      <span
        className={cn(
          "flex h-[34px] w-[100px] flex-shrink-0 items-center rounded-[8px] border border-[#dedfde] dark:border-[#333333] p-1 duration-300 ease-in-out",
          "after:h-[24px] after:w-[44px] after:rounded-md dark:after:bg-[#333333] after:shadow-sm after:duration-300 after:border dark:after:border-[#333333] after:border-[#666666]/100 after:bg-gradient-to-b after:from-[#3286F1] after:to-[#C33AC3] after:opacity-20 dark:after:opacity-100 dark:after:bg-none",
          "indeterminate:after:hidden",
          {
            "after:hidden": !site,
            "after:translate-x-[46px]": site === "TRPG",
          }
        )}
      />

      <span
        className={cn(
          "z-50 absolute p-1 text-sm flex justify-between text-center w-[100px] text-[#666666] dark:text-[#888888]",
          { "hover:text-black dark:hover:text-white": site }
        )}
      >
        <SiteSwitcherLink href="/AI" text="AI" isActive={site === "AI"} />
        <SiteSwitcherLink href="/TRPG" text="TRPG" isActive={site === "TRPG"} />
      </span>
    </div>
  );
}

export default SiteSwitcher;
