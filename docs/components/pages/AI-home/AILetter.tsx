import { HeroText } from "../home-shared/Headings";
import Image from "next/image";
import cn from "classnames";
import gradients from "../home-shared/gradients.module.css";
import { FadeIn } from "../home-shared/FadeIn";
import { CTAButton } from "../home-shared/CTAButton";
import Link from "next/link";
import { Gradient } from "../home-shared/Gradient";

export function AILetter() {
  return (
    <section className="relative flex flex-col items-center px-6 py-16 font-sans md:py-24 lg:py-32 gap-14">
      <FadeIn>
        <HeroText className="lg:text-[65px]">
          优化完善你的骰子系统
          <br />
          不再那么死板繁琐
        </HeroText>
      </FadeIn>
      <div className="flex flex-col max-w-xl leading-6 md:text-lg lg:text-lg">
        <FadeIn className="opacity-70">
          <p>
            当你的骰子系统越来越大，跑的团也越来越多且趋于复杂时，你会发现你的骰子系统越来越难以维护，越来越难以使用。
            HydroRollAI提供了很多工具，帮助你优化你的骰子系统，比如文本分析，自动化生成，自动化测试等等。
          </p>
          <br />
          <p>
            你可以写一整套完整的自动化流程，也可以只使用其中的一部分，HydroRollAI会按照你的流程自动去测试你的骰子系统，找出其中的问题。
            同时，HydroRollAI也会帮助你生成文档，让你的骰子系统更加易于使用。
            整个流程是并行的，你可以在任何时候停止，或者在任何时候加入新的流程。
          </p>
          <br />
          <p>我们还需要点其他的什么东西。</p>
          <br></br>
          <p>
            一种新颖的骰子系统，可以让你的骰子系统更加灵活，更加易于使用。
          </p>
          <br />
          <p>通过HydroRollAI，处理骰子系统就是那么简单处理。</p>
          <br />
          <p>
            你可以在HydroRollAI的文档中找到更多关于HydroRollAI的信息，或者你可以直接开始使用HydroRollAI。
          </p>
        </FadeIn>
        <FadeIn noVertical viewTriggerOffset className="relative h-2 md:h-12">
          <span
            className={cn(
              "w-full h-[1px] -bottom-8 md:-bottom-4 lg:-bottom-4 absolute",
              gradients.letterLine
            )}
          />
        </FadeIn>
        <FadeIn
          viewTriggerOffset
          noVertical
          className="flex items-end justify-center gap-3  md:self-start md:-ml-4 lg:self-start lg:-ml-4 min-w-[300px]"
        >
          <div className="w-24 h-24 min-w-[96px] min-h-[96px] rounded-full border dark:border-white/10 border-black/10 flex items-center justify-center ">
            <Image
              alt="Image of Jared Palmer"
              src="https://github.com/Stardust-minus.png"
              width={64}
              height={64}
              className="rounded-full grayscale"
            />
          </div>
          <div className="flex flex-col">
            <Image
              alt="Jared Palmer's hand written signature"
              src="/images/docs/AI/jared-signature-light.svg"
              width={190}
              height={90}
              className="block mt-3 mb-4 ml-3 dark:hidden"
            />
            <Image
              alt="Jared Palmer's hand written signature"
              src="/images/docs/AI/jared-signature-dark.svg"
              width={209}
              height={116}
              className="hidden -mt-2 dark:block"
            />
            <div className="flex gap-2 flex-wrap text-sm leading-none text-[#888888] max-w-[156px] md:max-w-xl lg:max-w-xl">
              <p className="font-bold">星尘(Stardust)</p>
              <p>水系模型训练者之一</p>
            </div>
          </div>
        </FadeIn>
      </div>
      <FadeIn noVertical className="relative flex justify-center w-full mt-16">
        <div className="max-w-[180px] w-full">
          <CTAButton>
            <Link href="/AI/docs" className="block py-3 font-sans">
              开始训练
            </Link>
          </CTAButton>
        </div>
        <Gradient
          width={1200}
          height={300}
          className="bottom-[-200px] -z-10 opacity-20"
          conic
        />
      </FadeIn>
    </section>
  );
}
