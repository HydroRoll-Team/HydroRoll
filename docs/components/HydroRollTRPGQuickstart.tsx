import {
  LightBulbIcon,
  QuestionMarkCircleIcon,
} from "@heroicons/react/outline";
import { DetailedFeatureLink } from "./Feature";

export const HydroRollTRPGQuickstartArea = () => {
  return (
    <div className="grid grid-cols-1 mt-12 gap-x-6 gap-y-12 sm:grid-cols-2 lg:mt-16 lg:gap-x-8 lg:gap-y-12">
      <DetailedFeatureLink
        feature={{
          Icon: QuestionMarkCircleIcon,
          description: `Learn why we created Turbopack, and why we think it’s the future of bundling for the web.`,
          name: "Why TRPG?",
        }}
        href="/TRPG/docs/why-trpg"
      ></DetailedFeatureLink>
      <DetailedFeatureLink
        feature={{
          Icon: LightBulbIcon,
          description: `Learn about the innovative architecture that powers TRPG’s speed improvements.`,
          name: "Core Concepts",
        }}
        href="/TRPG/docs/core-concepts"
      ></DetailedFeatureLink>
    </div>
  );
};
