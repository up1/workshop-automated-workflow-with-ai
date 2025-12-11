from fastapi import FastAPI
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

app = FastAPI()

@app.get("/data")
async def get_data():
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

        # Return the extracted content
        return {"data": result.markdown}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
