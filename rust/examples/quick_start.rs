use crawlora_imdb::{Client, ImdbSearchParams, ModelImdbSearchResponseDoc};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .imdb
        .search(ImdbSearchParams {
            query: Some("Inception".to_owned()),
            ..Default::default()
        })
        .await?;
    let data: ModelImdbSearchResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
