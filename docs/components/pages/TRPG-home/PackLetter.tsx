import { HeroText } from "../home-shared/Headings";
import Image from "next/image";
import cn from "classnames";
import gradients from "../home-shared/gradients.module.css";
import { FadeIn } from "../home-shared/FadeIn";
import { CTAButton } from "../home-shared/CTAButton";
import Link from "next/link";
import { Gradient } from "../home-shared/Gradient";

export function PackLetter() {
  return (
    <section className="relative flex flex-col items-center px-6 py-16 font-sans md:py-24 lg:py-32 gap-14">
      <FadeIn>
        <HeroText>
          究竟什么才是真正的
          <br />
          水系?
        </HeroText>
      </FadeIn>
      <div className="flex flex-col max-w-xl leading-6 md:text-lg lg:text-lg">
        <FadeIn className="opacity-70">
          <p>
            当水系公测后，我接触TRPG已经有两年多了，我希望能够在这里分享一些我对TRPG的理解。
            TRPG，是一种游戏，也是一种文化，它的核心是“故事”。究竟要怎么讲好一个故事呢？我认为，一个好的故事，应该是有趣的，有趣的故事，才能吸引人，才能让人愿意去听，去看，去玩。
          </p>
          <br />
          <p>
            但是，有趣的故事，不是随随便便就能讲好的，它需要有一个好的故事背景，需要有一个好的故事情节，需要有一个好的故事结局。这些，都是一个好的故事所必须具备的。
            水系其实是站在规则书作者的角度去设计的，它的第一服务对象永远是世界主，再是kp与pl们。所以，水系的设计，是为了让世界主们能够更好的描绘自己所想象的那个世界。
          </p>
          <br />
          <p>
            水系是自由的，这主要表现在规则书是以热插拔规则包的形式存在的，世界主们可以根据自己的需要，自由的编写自己想要的规则包，来丰富自己的世界。水系是开放的，这主要表现在规则书的开源，世界主们可以根据自己的需要，自由的修改规则书，来丰富自己的世界。
            总之，水系是为世界主们服务的，水系的目的，就是让世界主们能够更好的讲好自己的故事，构建好自己的世界。让更多冷门世界观与规则书得到更多人的关注，让更多人能够参与到TRPG的世界中来。
          </p>
        </FadeIn>
        <FadeIn
          noVertical
          viewTriggerOffset
          className="relative h-2 md:h-12 lg:h-12"
        >
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
          className="flex items-end justify-center gap-3 md:self-start md:-ml-4 lg:self-start lg:-ml-4 min-w-[300px]"
        >
          <div className="w-24 h-24 min-w-[96px] min-h-[96px] rounded-full border dark:border-white/10 border-black/10 flex items-center justify-center ">
            <Image
              alt="Image of Tobias Koopers"
              src="/images/people/HsiangNianian.jpg"
              width={64}
              height={64}
              className="rounded-full"
            />
          </div>
          <div className="flex flex-col gap-3 pb-2">
            <Image
              alt="Tobias Koppers hand written signature"
              src="/images/docs/TRPG/tobias-signature-light.svg"
              // 16 px added and offset to account for the glow
              width={173 + 16}
              height={91 + 16}
              className="block -mb-3 -ml-3 dark:hidden"
            />
            {/* <Image
              alt="Tobias Koppers hand written signature"
              src="/images/docs/TRPG/tobias-signature-dark.svg"
              // 16 px added and offset to account for the glow
              width={173 + 16}
              height={91 + 16}
              className="hidden -mb-3 -ml-3 dark:block"
            /> */}
            <div className="flex gap-2 flex-wrap text-sm leading-none text-[#888888] max-w-[156px] md:max-w-xl lg:max-w-xl">
              <p className="font-bold">简律纯(HsiangNianian)</p>
              <p>Creator of HydroRoll</p>
            </div>
          </div>
        </FadeIn>
      </div>
      <FadeIn noVertical className="relative flex justify-center w-full mt-16">
        <div className="max-w-[180px] w-full">
          <CTAButton>
            <Link href="/TRPG/docs" className="block py-3 font-sans">
              Start Building
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
