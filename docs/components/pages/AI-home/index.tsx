import { AIHero } from "./AIHero";
import { AIFeatures } from "./AIFeatures";
import { AILetter } from "./AILetter";
import { GradientSectionBorder } from "../home-shared/GradientSectionBorder";
import { LandingPageGlobalStyles } from "../home-shared/GlobalStyles";

export default function HydroRollAIHome() {
  return (
    <>
      <LandingPageGlobalStyles />
      <main className="relative">
        <AIHero />
        <GradientSectionBorder>
          <AIFeatures />
        </GradientSectionBorder>
        <GradientSectionBorder>
          <AILetter />
        </GradientSectionBorder>
      </main>
    </>
  );
}
