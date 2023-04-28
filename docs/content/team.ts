const TURBO_TEAM: Record<string, AuthorDetails> = {
  HsiangNianian: {
    name: "简律纯",
    twitterUsername: "HsiangNianian",
    picture: "/images/people/HsiangNianian.jpg",
  },
};

export type Author = keyof typeof TURBO_TEAM;
export type AuthorDetails = {
  name: string;
  twitterUsername?: string;
  picture: string;
};

export default TURBO_TEAM;
