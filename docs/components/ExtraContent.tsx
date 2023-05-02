import RemoteCacheCounter from "./RemoteCacheCounter";
import { useTurboSite } from "./SiteSwitcher";

export default function ExtraContent() {
  const site = useTurboSite();

  if (site === "AI") {
    return <RemoteCacheCounter />;
  }
}
