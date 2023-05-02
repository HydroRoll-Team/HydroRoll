import { DiscordIcon, GitHubIcon } from "nextra/icons";

function Github() {
  return (
    <a
      href="https://github.com/retrofor/HydroRoll"
      className="hidden p-2 text-current sm:flex hover:opacity-75"
      title="HydroRoll GitHub repo"
      target="_blank"
      rel="noreferrer"
    >
      {/* Nextra icons have a <title> attribute providing alt text */}
      <GitHubIcon />
    </a>
  );
}

function Discord() {
  return (
    <a
      href="https://hydroroll.retrofor.space/discord"
      className="hidden p-2 text-current sm:flex hover:opacity-75"
      title="HydroRoll Discord server"
      target="_blank"
      rel="noreferrer"
    >
      <DiscordIcon />
    </a>
  );
}

export { Github, Discord };
