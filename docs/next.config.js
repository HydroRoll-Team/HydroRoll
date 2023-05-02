const { withSentryConfig } = require("@sentry/nextjs");
const withNextra = require("nextra")({
  theme: "nextra-theme-docs",
  themeConfig: "./theme.config.js",
  unstable_flexsearch: true,
  unstable_staticImage: true,
});

const sentryWebpackPluginOptions = {
  silent: true,
};

const OLD_TURBOREPO_ROUTES = [
  "/docs",
  "/docs/getting-started/create-new",
  "/docs/getting-started/existing-monorepo",
  "/docs/acknowledgements",
  "/docs/faq",
  "/docs/troubleshooting",
];

const nextConfig = withNextra({
  sentry: {
    autoInstrumentServerFunctions: false,
    hideSourceMaps: true,
  },
  reactStrictMode: true,
  experimental: {
    legacyBrowsers: false,
  },
  webpack: (config, { webpack }) => {
    config.plugins.push(
      new webpack.DefinePlugin({
        __SENTRY_DEBUG__: false,
        __SENTRY_TRACING__: false,
      })
    );

    // return the modified config
    return config;
  },
  rewrites() {
    return {
      beforeFiles: [
        {
          source: "/sitemap.xml",
          destination:
            "https://crawled-sitemap.vercel.sh/turbobuild-sitemap.xml",
        },
      ],
    };
  },
  async redirects() {
    return [
      ...OLD_TURBOREPO_ROUTES.map((route) => ({
        source: route,
        destination: `/AI${route}`,
        permanent: true,
      })),
      {
        source: "/docs/getting-started",
        destination: "/AI/docs",
        permanent: true,
      },
      {
        source: "/discord{/}?",
        permanent: true,
        destination: "https://discord.gg/JBe8BYJgKT",
      },
      {
        source: "/docs/changelog",
        permanent: true,
        destination: "https://github.com/retrofor/HydroRoll/releases",
      },
      {
        // Accidentally created, eventually removable. See below.
        source: "/AI/docs/getting-started",
        destination: "/AI/docs",
        permanent: true,
      },
      {
        // This rule accidentally created a bunch of URLs.
        //
        // They've _never_ resolved, so _eventually_ we should be able to remove the
        // redirects we added above to fix them.
        source: "/docs/:path*",
        permanent: true,
        destination: "/AI/docs/:path*",
      },
    ];
  },
});

module.exports = withSentryConfig(nextConfig, sentryWebpackPluginOptions);
