import { useState } from "react";
import { FadeIn } from "../home-shared/FadeIn";
import { SectionHeader, SectionSubtext } from "../home-shared/Headings";
import { BenchmarksGraph } from "./PackBenchmarksGraph";
import { PackBenchmarksPicker } from "./PackBenchmarksPicker";
import { PackBenchmarkTabs } from "./PackBenchmarkTabs";

export type BenchmarkNumberOfModules = "1000" | "5000" | "10000" | "30000";
export type BenchmarkCategory =
  | "cold"
  | "from_cache"
  | "file_change"
  | "code_build"
  | "build_from_cache";
export interface BenchmarkData {
  HydroRoll水系: number;
  溯洄Shiki: number;
  OlivOS青果: number;
  SealDice海豹: number;
}

export interface BenchmarkBar {
  label: string;
  key: keyof BenchmarkData;
  turbo?: true;
  swc?: true;
}

export const DEFAULT_BARS: BenchmarkBar[] = [
  {
    key: "HydroRoll水系",
    label: "HydroRoll水系 CQHTTP",
    turbo: true,
  },
  {
    key: "溯洄Shiki",
    label: "溯洄Shiki GocqLite",
  },
  {
    key: "OlivOS青果",
    label: "OlivOS青果 onebot",
    swc: true,
  },
  {
    key: "SealDice海豹",
    label: "SealDice海豹 qq",
  },
];
export const HMR_BARS: BenchmarkBar[] = [
  {
    key: "HydroRoll水系",
    label: "HydroRoll水系 CQHTTP",
    turbo: true,
  },
  {
    key: "溯洄Shiki",
    label: "溯洄Shiki GocqLite",
    swc: true,
  },
  {
    key: "OlivOS青果",
    label: "OlivOS青果 onebot",
  },
  {
    key: "SealDice海豹",
    label: "SealDice海豹 qq",
  },
];

export function PackBenchmarks() {
  const [numberOfModules, setNumberOfModules] =
    useState<BenchmarkNumberOfModules>("1000");
  const [category, setCategory] = useState<BenchmarkCategory>("cold");

  return (
    <FadeIn className="relative flex flex-col items-center justify-center w-full gap-10 py-16 font-sans md:py-24 lg:py-32">
      <div className="flex flex-col items-center gap-5 md:gap-6">
        <SectionHeader>比快更快</SectionHeader>
        <SectionSubtext>
          Crafted by the creators of Webpack, Turbopack delivers unparalleled
          performance at scale.
        </SectionSubtext>
      </div>
      <div className="flex flex-col items-center w-full">
        <PackBenchmarkTabs onTabChange={setCategory} />
        <BenchmarksGraph
          category={category}
          numberOfModules={numberOfModules}
          bars={DEFAULT_BARS}
        />
      </div>
      <PackBenchmarksPicker
        setNumberOfModules={setNumberOfModules}
      ></PackBenchmarksPicker>
    </FadeIn>
  );
}
