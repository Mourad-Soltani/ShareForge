# Optional Python CLI entry point
# Built by Mourad.Soltani
import argparse
from shareforge.generator import generate_meta_tags

def main():
    p = argparse.ArgumentParser(description="ShareForge CLI — generate meta tags")
    p.add_argument("--title", required=True)
    p.add_argument("--description", required=True)
    p.add_argument("--image")
    p.add_argument("--site")
    p.add_argument("--url")
    args = p.parse_args()
    print(generate_meta_tags(
        title=args.title,
        description=args.description,
        image_url=args.image,
        site_name=args.site,
        url=args.url,
    ))

if __name__ == "__main__":
    main()
