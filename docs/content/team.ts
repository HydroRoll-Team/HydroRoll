const HYDROROLL_TEAM: Record<string, AuthorDetails> = {
  HsiangNianian: {
    name: "简律纯",
    GithubUsername: "HsiangNianian",
    picture: "/images/people/HsiangNianian.jpg",
  },
};

export type Author = keyof typeof HYDROROLL_TEAM;
export type AuthorDetails = {
  name: string;
  GithubUsername?: string;
  picture: string;
};

export default HYDROROLL_TEAM;
