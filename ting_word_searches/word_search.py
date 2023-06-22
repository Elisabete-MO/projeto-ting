def exists_word(word, instance):
    results = []

    for file_data in instance.queue:
        file_name = file_data["nome_do_arquivo"]
        lines_with_word = []

        for line_num, line in enumerate(file_data["linhas_do_arquivo"],
                                        start=1):
            if word.lower() in line.lower():
                lines_with_word.append({"linha": line_num})

        if lines_with_word:
            file_result = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": lines_with_word
            }
            results.append(file_result)

    return results


def search_by_word(word, instance):
    results = []

    for file_data in instance.queue:
        file_name = file_data["nome_do_arquivo"]
        lines_with_word = []

        for line_num, line_content in enumerate(file_data["linhas_do_arquivo"],
                                                start=1):
            if word.lower() in line_content.lower():
                line_result = {
                    "linha": line_num,
                    "conteudo": line_content.strip()
                }
                lines_with_word.append(line_result)

        if lines_with_word:
            file_result = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": lines_with_word
            }
            results.append(file_result)

    return results
