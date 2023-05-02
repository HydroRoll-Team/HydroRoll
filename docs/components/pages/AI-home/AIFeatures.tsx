import { REPO_HOME_FEATURES } from "../../../content/features";
import { FadeIn } from "../home-shared/FadeIn";
import { FeaturesBento } from "../home-shared/FeaturesBento";

export function AIFeatures() {
  return (
    <FadeIn className="py-16 md:py-24 lg:py-32">
      <FeaturesBento
        header="Why AI?"
        body="AI balabala..."
        features={REPO_HOME_FEATURES}
      />
    </FadeIn>
  );
}
