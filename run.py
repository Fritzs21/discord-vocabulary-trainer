from dcvocabulary import VocabularyTrainer


if __name__ == "__main__":
    bot = VocabularyTrainer()
    with open(".gitignore", "r") as f:
        token = f.read()
    bot.run(token)
