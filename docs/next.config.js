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
  "/docs/ci/circleci",
  "/docs/ci/github-actions",
  "/docs/ci/gitlabci",
  "/docs/ci/travisci",
  "/docs/core-concepts/caching",
  "/docs/core-concepts/remote-caching",
  "/docs/core-concepts/scopes",
  "/docs/core-concepts/monorepos/filtering",
  "/docs/core-concepts/monorepos/running-tasks",
  "/docs/getting-started/create-new",
  "/docs/getting-started/existing-monorepo",
  "/docs/handbook",
  "/docs/handbook/building-your-app",
  "/docs/handbook/deploying-with-docker",
  "/docs/handbook/dev",
  "/docs/handbook/linting",
  "/docs/handbook/migrating-to-a-monorepo",
  "/docs/handbook/package-installation",
  "/docs/handbook/publishing-packages",
  "/docs/handbook/sharing-code",
  "/docs/handbook/testing",
  "/docs/handbook/troubleshooting",
  "/docs/handbook/what-is-a-monorepo",
  "/docs/handbook/workspaces",
  "/docs/handbook/linting/eslint",
  "/docs/handbook/linting/typescript",
  "/docs/handbook/publishing-packages/bundling",
  "/docs/handbook/publishing-packages/versioning-and-publishing",
  "/docs/handbook/sharing-code/internal-packages",
  "/docs/reference/codemods",
  "/docs/reference/command-line-reference",
  "/docs/reference/configuration",
  "/docs/acknowledgements",
  "/docs/ci",
  "/docs/faq",
  "/docs/troubleshooting",
  "/docs/upgrading-to-v1",
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
        destination: `/repo${route}`,
        permanent: true,
      })),
      {
        source: "/docs/getting-started",
        destination: "/repo/docs",
        permanent: true,
      },
      {
        source: "/usage",
        destination: "/repo/docs/reference/command-line-reference",
        permanent: true,
      },
      {
        source: "/docs/core-concepts/running-tasks",
        destination: "/repo/docs/core-concepts/monorepos/running-tasks",
        permanent: true,
      },
      {
        source: "/docs/core-concepts/why-turborepo",
        destination: "/repo/docs/core-concepts/monorepos",
        permanent: true,
      },
      {
        source: "/docs/core-concepts/filtering",
        destination: "/repo/docs/core-concepts/monorepos/filtering",
        permanent: true,
      },
      {
        source: "/docs/guides/workspaces",
        destination: "/repo/docs/handbook/workspaces",
        permanent: true,
      },
      {
        source: "/docs/core-concepts/workspaces",
        destination: "/repo/docs/handbook/workspaces",
        permanent: true,
      },
      {
        source: "/docs/core-concepts/pipelines",
        destination: "/repo/docs/core-concepts/monorepos/running-tasks",
        permanent: true,
      },
      {
        source: "/docs/guides/migrate-from-lerna",
        destination: "/repo/docs/handbook/migrating-to-a-monorepo",
        permanent: true,
      },
      {
        source: "/discord{/}?",
        permanent: true,
        destination: "https://discord.gg/sSzyjxvbf5",
      },
      {
        source: "/docs/changelog",
        permanent: true,
        destination: "https://github.com/vercel/turbo/releases",
      },
      {
        source: "/docs/guides/complimentary-tools",
        permanent: true,
        destination: "/repo/docs/handbook",
      },
      {
        source: "/docs/guides/monorepo-tools",
        permanent: true,
        destination: "/repo/docs/handbook",
      },
      {
        source: "/docs/glossary",
        permanent: true,
        destination: "/repo/docs/handbook",
      },
      {
        source: "/docs/guides/continuous-integration",
        permanent: true,
        destination: "/repo/docs/ci",
      },
      {
        source: "/repo/docs/handbook/prisma",
        permanent: true,
        destination: "/repo/docs/handbook/tools/prisma",
      },
      {
        source: "/pack/docs/comparisons/turbopack-vs-vite",
        permanent: true,
        destination: "/pack/docs/comparisons/vite",
      },
      {
        source: "/pack/docs/comparisons/turbopack-vs-webpack",
        permanent: true,
        destination: "/pack/docs/comparisons/webpack",
      },
      {
        // Accidentally created, eventually removable. See below.
        source: "/repo/docs/core-concepts/running-tasks",
        destination: "/repo/docs/core-concepts/monorepos/running-tasks",
        permanent: true,
      },
      {
        // Accidentally created, eventually removable. See below.
        source: "/repo/docs/core-concepts/why-turborepo",
        destination: "/repo/docs/core-concepts/monorepos",
        permanent: true,
      },
      {
        // Accidentally created, eventually removable. See below.
        source: "/repo/docs/core-concepts/filtering",
        destination: "/repo/docs/core-concepts/monorepos/filtering",
        permanent: true,
      },
      {
        // Accidentally created, eventually removable. See below.
        source: "/repo/docs/core-concepts/pipelines",
        destination: "/repo/docs/core-concepts/monorepos/running-tasks",
        permanent: true,
      },
      {
        // This rule accidentally created a bunch of URLs.
        //
        // They've _never_ resolved, so _eventually_ we should be able to remove the
        // redirects we added above to fix them.
        source: "/docs/features/:path*",
        permanent: true,
        destination: "/repo/docs/core-concepts/:path*",
      },
      {
        // Accidentally created, eventually removable. See below.
        source: "/repo/docs/getting-started",
        destination: "/repo/docs",
        permanent: true,
      },
      {
        // Accidentally created, eventually removable. See below.
        source: "/repo/docs/guides/workspaces",
        destination: "/repo/docs/handbook/workspaces",
        permanent: true,
      },
      {
        // This rule accidentally created a bunch of URLs.
        //
        // They've _never_ resolved, so _eventually_ we should be able to remove the
        // redirects we added above to fix them.
        source: "/docs/:path*",
        permanent: true,
        destination: "/repo/docs/:path*",
      },
    ];
  },
});

module.exports = withSentryConfig(nextConfig, sentryWebpackPluginOptions);
