import { PACK_HOME_FEATURES } from "../../../content/features";
import { FeaturesBento } from "../home-shared/FeaturesBento";

export function PackFeatures() {
  return (
    <FeaturesBento
      header="Why HydroRollCore?
      为什么选择水系核心?"
      body="水系核心基于规则包运行，可自定义程度高，且运行速率快。"
      features={PACK_HOME_FEATURES}
    />
  );
}
