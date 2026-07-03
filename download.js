import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://v22.www-y2mate.com/');
  await page.getByRole('textbox', { name: 'Search or paste link here...' }).dblclick();
  await page.getByRole('textbox', { name: 'Search or paste link here...' }).fill('https://youtube.com/shorts/tHtQwObI-XM?si=R9_CYPKdvAYJd1Dr');
  await page.getByRole('textbox', { name: 'Search or paste link here...' }).press('Enter');
  await page.locator('#widgetv2Api').contentFrame().getByRole('link', { name: 'Video' }).click();
  const page1Promise = page.waitForEvent('popup');
  await page.locator('#widgetv2Api').contentFrame().getByRole('row', { name: '1080p (.mp4) Auto  Download' }).getByRole('button').click();
  const page1 = await page1Promise;
  const page2Promise = page.waitForEvent('popup');
  const downloadPromise = page.waitForEvent('download');
  await page.locator('#widgetv2Api').contentFrame().getByRole('link', { name: 'Download' }).click();
  const page2 = await page2Promise;
  const download = await downloadPromise;
  await download.saveAs('./youtubedownloads/' + download.suggestedFilename());
});
