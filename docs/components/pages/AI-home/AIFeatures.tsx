import { REPO_HOME_FEATURES } from "../../../content/features";
import { FadeIn } from "../home-shared/FadeIn";
import { FeaturesBento } from "../home-shared/FeaturesBento";

export function AIFeatures() {
  return (
    <FadeIn className="py-16 md:py-24 lg:py-32">
      <FeaturesBento
        header="为什么使用模型?"
        body="模型, 一种可以用来预测未来的工具."
        features={REPO_HOME_FEATURES}
      />
    </FadeIn>
  );
}
