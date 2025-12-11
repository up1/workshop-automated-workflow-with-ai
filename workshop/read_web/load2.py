import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

async def main():

    config = CrawlerRunConfig(
        css_selector="#dr-overview-tab-search > div > div.dr-overview-search-TradingInformation > div.layout-result-table > div.dr-table.layout-result-table > div",
        word_count_threshold=10,
    )

    # Create an instance of AsyncWebCrawler
    async with AsyncWebCrawler() as crawler:
        # Run the crawler on a URL
        result = await crawler.arun(
            url="https://www.set.or.th/th/market/product/dr/marketdata",
            config=config,
        )

        # Print the extracted content
        print(result.markdown)

# Run the async main function
asyncio.run(main())
