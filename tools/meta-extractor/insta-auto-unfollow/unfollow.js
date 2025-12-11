const puppeteer = require("puppeteer");
const readline = require("readline");

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    executablePath: "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    userDataDir: "./braveProfile", // keeps you logged into Instagram
  });
  const page = await browser.newPage();

  // Load your local file
  await page.goto("file:///Users/I566972/Desktop/instagram-md.zouari-2025-09-28-UShX7e4j/connections/followers_and_following/recent_follow_requests.html");

  // Collect all profile links
  const links = await page.$$eval("a", as =>
    as.filter(a => a.href.includes("instagram.com")).map(a => a.href)
  );

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    prompt: 'Press ENTER to view next profile: '
  });

  let currentIndex = 0;

  rl.prompt();

  rl.on('line', async () => {
    if (currentIndex < links.length) {
      const link = links[currentIndex];
      const tab = await browser.newPage();
      console.log(`Opening link: ${link}`);
      await tab.goto(link, { waitUntil: "networkidle2" });

      try {
        // 1. Click "Requested"
        await tab.waitForSelector('button:has-text("Requested")', { timeout: 5000 });
        await tab.click('button:has-text("Requested")');

        // 2. Click "Unfollow" in the dialog
        await tab.waitForSelector('button:has-text("Unfollow")', { timeout: 5000 });
        await tab.click('button:has-text("Unfollow")');

        await tab.waitForTimeout(1000);
      } catch (err) {
        console.error(`❌ Error processing ${link}`, err);
      }

      await tab.close();
      currentIndex++;
      rl.prompt();
    } else {
      console.log('No more links to process.');
      rl.close();
      await browser.close();
    }
  });
})();