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
            Since the public beta of Water System, I have been involved in TRPG for over two years, and I would like to share some of my understanding of TRPG here.
            TRPG is not only a game but also a culture. Its core is "storytelling." How can we tell a good story? In my opinion, a good story should be interesting. An interesting story can attract people's attention and make them willing to listen, watch, and play.
          </p>
          <br />
          <p>
            However, it is not easy to tell an interesting story. It needs a good story background, a good story plot, and a good story ending. These are all necessary for a good story. Water System is designed from the perspective of rulebook authors. Its primary audience is world masters, followed by game masters and players. Therefore, the design of Water System aims to help world masters better depict the world they imagine.
          </p>
          <br />
          <p>
            Water System is free, mainly manifested in the form of hot-swappable rulebook packages. World masters can freely write their own rulebook packages to enrich their world according to their needs. Water System is open, mainly manifested in the open-source nature of the rulebook. World masters can freely modify the rulebook to enrich their world according to their needs.
            In short, Water System is here to serve world masters. The purpose of Water System is to help world masters tell their stories better and build their own worlds. It aims to bring more attention to niche world views and rulebooks and allow more people to participate in the world of TRPG.
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
