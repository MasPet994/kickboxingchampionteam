const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://kickboxing-championteam.web.app/?v=5', { waitUntil: 'networkidle' });
  await page.setViewportSize({ width: 1280, height: 800 });
  
  // Scroll to sponsors section
  await page.evaluate(() => {
    document.getElementById('sponsors').scrollIntoView();
  });
  
  // Wait a moment for scroll and animation
  await page.waitForTimeout(1000);
  
  // Capture screenshot of the scrolling state
  await page.screenshot({ path: 'C:/Users/DELL/.gemini/antigravity/brain/89a8788b-b98b-4465-9e80-db0a8659bd4b/sponsors_carousel.png' });
  
  // Hover over the first sponsor logo to trigger the golden glow and pause
  await page.hover('.sponsor-logo');
  await page.waitForTimeout(500); // Wait for transition
  
  // Capture screenshot of the hover state
  await page.screenshot({ path: 'C:/Users/DELL/.gemini/antigravity/brain/89a8788b-b98b-4465-9e80-db0a8659bd4b/sponsors_carousel_hover.png' });
  
  await browser.close();
})();
