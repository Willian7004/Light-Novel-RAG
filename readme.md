中文版本：
本项目用于调用LLM对小说或记叙文进行总结和查询。目标是解决常规rag方法只能读取部分文段和不能精确定位需要获取原文的文段的问题。在导入一本书时需要略多于全文的token对内容进行总结，进行查询时由于只需要传入总结的内容和部分原文，使用的token数不会明显多于常规rag方法。
运行前应当把要总结的内容放到 book.txt ，并创建文件夹“chapter”、”chapter2”、“summarize”、“summarize2”。使用前需要在 api.py 对api进行设置。为了确保输出内容符合要求，建议使用Deepseek Coder v2或其它逻辑能力接近的LLM，这类LLM也可以对本项目进行辅助开发和维护。开发程序中各文件的对话内容在同名txt文件，api.py没有使用LLM辅助开发。
项目中的文件按功能命名，使用程序时应当先运行 分割.py （默认匹配'------------'字符。应当根据book.txt中用于分割的字符进行调整）和 总结.py ，得到对每个分段的第一级总结。 连接1.py 用于把第一级总结的内容连接为更长的分段，再由 总结2.py 进行第二级总结并提取关键词。第二级总结完成后运行 连接2.py 得到summarize2.txt 。如果不需要进行第二级总结，应当运行 连接.py 得到 summarize.txt 。
搜索1.py 用于从第一级总结中搜索内容，如果模型请求获取原文部分内容，会传入对应内容并打印，之后LLM通过获取的原文回答问题。 搜索2.py 用于从第二级总结中搜索内容，如果模型请求获取第一级总结的内容，会传入对应内容并并打印，后续步骤与 搜索1.py 类似。
项目包含多个语言的版本，均使用LLM进行翻译。仓库中单独的文件只包含中文版本，其它语言的版本为压缩包。翻译的内容包括说明、需要运行的文件的文件名（除中文版本外均使用英文文件名）和提示词（包括api.py和创建文件的提示词）。其它文件和文件夹仍然使用英文。另外，为了避免LLM在翻译混淆任务，保存提示词的文件中去掉了要求开发python程序的句子。如果您发现翻译有误，可以进行修改并提交。

测试结果：使用Deepseek Coder v2能完成总结任务，但召回时测试了多个问题，模型均没有请求获取原文内容，只基于概括内容进行回答。如果大家有其它模型的api可以进一步测试，也可以给出修改建议。



English version：
This project aims to utilize LLMs for summarizing and querying novels or narrative texts. It addresses the limitations of conventional RAG methods, which can only read partial text segments and struggle to pinpoint the exact segments needed for retrieval.

**Project Workflow:**

1. **Preprocessing:** Place the text you want to summarize in "book.txt". Create folders named "chapter", "chapter2", "summarize", and "summarize2".
2. **Configuration:** Set up the API in "api.py". 
3. **Summarization:** Run "split.py" (default delimiter is '------------', adjust if needed) followed by "summarize.py" to generate first-level summaries for each segment.
4. **Refinement (Optional):** Run "connect1.py" to combine first-level summaries into longer segments, then execute "summarize2.py" for second-level summarization and keyword extraction. The final summarized output will be in "summarize2.txt". If second-level summarization is not required, run "connect.py" for the "summarize.txt" output.
5. **Querying:** 
   *  Run "search1.py" to query from first-level summaries. When the model requests specific text segments, they will be retrieved and printed, allowing the LLM to answer questions based on the provided context.
   * Run "search2.py" to query from second-level summaries (if generated). Similar to "search1.py", it retrieves relevant text segments for the LLM's response.

**LLM Recommendations:**

For optimal results, use Deepseek Coder v2 or other LLMs with comparable reasoning capabilities. These models can also assist in developing and maintaining this project.

**Project Structure & Files:**

Each file is named based on its function. 
* Dialogue content from development files is stored in corresponding .txt files (except "api.py", which was not LLM-assisted).


**Language Support:**

The repository contains versions in multiple languages, all translated using LLMs. The standalone files only include the Chinese version; other language versions are provided as compressed packages. Translations encompass instructions, file names (excluding the Chinese version), and prompts (including those in "api.py" and file creation instructions). Other files and folders retain English names.

To prevent LLM translation ambiguity during task execution,  prompts requiring Python program development were removed from the translated prompt files. Please contribute any identified translation errors for correction.

Test Results: 

Deepseek Coder v2 is capable of completing summarization tasks. However, during recall testing with multiple questions, the model did not request access to the original text in any case and only based its answers on the summarized content.

Further testing with APIs from other models would be beneficial. Suggestions for modifications are also welcome. 




Traduction Française：
Ce projet a pour objectif d'utiliser un LLM (Large Language Model) pour résumer et effectuer des recherches dans des romans ou des récits. Il vise à résoudre le problème des méthodes rag classiques qui ne peuvent lire qu'une partie du texte et ne peuvent pas précisément localiser les parties du texte dont il faut obtenir l'original. 

Lors de l'importation d'un livre, légèrement plus de jetons que la longueur totale du texte sont nécessaires pour effectuer un résumé. Lors des recherches, comme seuls le résumé et une partie du texte original sont transmis, le nombre de jetons utilisés n'excède pas sensiblement celui des méthodes rag classiques.

Avant l'exécution, il est nécessaire de placer le contenu à résumer dans "book.txt" et de créer les dossiers "chapter", "chapter2", "summarize" et "summarize2". Avant d'utiliser le programme, il est important de configurer l'API dans "api.py". Pour assurer une sortie conforme aux exigences, il est recommandé d'utiliser Deepseek Coder v2 ou un autre LLM avec des capacités logiques similaires. Ces types de modèles peuvent également aider au développement et à la maintenance du projet. 

Les conversations entre les fichiers du programme sont sauvegardées dans des fichiers txt portant le même nom. "api.py" n'a pas été développé avec l'aide d'un LLM.

Les fichiers du projet sont nommés en fonction de leur fonction. Lors de l'utilisation du programme, il faut d'abord exécuter "split.py" (qui correspond par défaut au caractère '------------'). Il est important d'ajuster ce paramètre en fonction du caractère utilisé pour la séparation dans "book.txt") et "summarize.py", pour obtenir un résumé de première niveau pour chaque segment. 

"connect1.py" est utilisé pour connecter les résumés de première niveau en segments plus longs, qui sont ensuite résumés au deuxième niveau par "summarize2.py" et les mots-clés sont extraits. Une fois le résumé de deuxième niveau terminé, exécutez "connect2.py" pour obtenir "summarize2.txt". Si vous n'avez pas besoin d'effectuer un résumé de deuxième niveau, exécutez "connect.py" pour obtenir "summarize.txt".

"search1.py" permet de rechercher du contenu dans les résumés de première niveau. Si le modèle demande une partie du texte original, le contenu correspondant est transmis et affiché, puis l'LLM répond à la question grâce au texte original reçu. 

"search2.py" permet de rechercher du contenu dans les résumés de deuxième niveau. Si le modèle demande le contenu des résumés de première niveau, il est transmis et affiché, les étapes suivantes étant similaires à celles de "search1.py".


Le projet comprend des versions dans plusieurs langues, toutes traduites par un LLM. Le dépôt contient uniquement la version chinoise en fichiers individuels, tandis que les autres versions sont disponibles sous forme de fichiers compressés. 

Les traductions incluent les instructions, les noms des fichiers à exécuter et les messages contextuels (y compris "api.py" et les messages contextuels pour la création de fichiers). Les autres fichiers et dossiers utilisent l'anglais.  De plus, afin d'éviter que l'LLM ne confonde les tâches lors de la traduction, les fichiers contenant les messages contextuels ont supprimé la phrase demandant le développement d'un programme Python. Si vous remarquez des erreurs de traduction, vous pouvez les corriger et les soumettre. 

Résultats du test : Deepseek Coder v2 est capable d'accomplir la tâche de résumé, mais lors des tests de rappel, plusieurs questions ont été posées et le modèle n'a pas sollicité l'accès au texte original à chaque fois. Il s'est basé uniquement sur le contenu résumée pour répondre. Si vous disposez d'autres API de modèles, il serait possible de les tester davantage et d'apporter des suggestions de modifications. 




Английская версия：
Данный проект предназначен для вызова LLM для резюме и поиска по рассказам или романам. Цель - решить проблему традиционных rag-методов, которые могут читать только фрагменты текста и не могут точно определить фрагменты, из которых требуется получить исходный текст. 

При импорте книги необходимо использовать немного больше токенов, чем полная длина текста, для создания резюме, а при поиске используется меньшее количество токенов, поскольку передаются только резюме и часть исходного текста.

Перед запуском необходимо поместить текст для резюмирования в файл "book.txt" и создать папки "chapter", "chapter2", "summarize", "summarize2".  Перед использованием необходимо настроить API в файле "api.py". Для обеспечения соответствия выходных данных требованиям рекомендуется использовать Deepseek Coder v2 или другой LLM с похожими логическими возможностями. Такие LLM также могут быть использованы для вспомогательного развития и обслуживания данного проекта. 

Диалоги между файлами в проекте сохранены в текстовых файлах с соответствующими именами. Разработка программы не использовала помощь LLM.

Файлы проекта названы по функциям, поэтому при использовании необходимо сначала запустить Split.py (по умолчанию он ищет символ '------------'.  Важно его настроить в соответствии со символом, используемым для разделения текста в "book.txt"), а затем Summarize.py, чтобы получить первое резюме каждого раздела. Connect1.py используется для объединения первых резюме в более длинные фрагменты, после чего Summarize2.py создает второе резюме и извлекает ключевые слова. После завершения второго уровня резюме запустите Connect2.py для получения файла "summarize2.txt". Если не требуется второе резюмирование, запустите Connect.py для получения файла "summarize.txt".

Search1.py используется для поиска информации в первом уровне резюме. Если модель запросит часть исходного текста, соответствующий фрагмент будет передан и выведен на печать. LLM отвечает на вопрос, получив доступ к предоставленному фрагменту текста. Search2.py используется для поиска информации во втором уровне резюме.  Если модель запросит информацию из первого уровня резюме, соответствующий фрагмент будет передан и выведен на печать, после чего выполняются действия, аналогичные Search1.py.

Проект содержит версии на нескольких языках, все они переведены с помощью LLM. В репозитории доступны отдельные файлы только для китайского варианта. Версии на других языках представлены в виде архивов. Перевод включает описание, названия файлов (кроме китайской версии), имена которых указаны на английском языке, и подсказки (включая "api.py" и подсказки по созданию файлов). Остальные файлы и папки продолжают использоваться на английском языке. Кроме того, для предотвращения путаницы LLM при переводе, в файлах с подсказками удалены предложения, связанные с разработкой программы на Python. Если вы обнаружите ошибки в переводе, вы можете внести их исправления и отправить изменения.

Результаты тестирования: 

Модель Deepseek Coder v2 справляется с задачей обобщения, однако при проверочном тесте на несколько вопросов модель не запрашивала исходный текст для ответа, основываясь исключительно на предоставленном кратком изложении.  

Если у вас есть API других моделей, можно провести дальнейшие тестирования и внести предложения по улучшению. 


Versión en España：
##  Proyecto de Resumen y Consulta de Novelas con LLM

Este proyecto utiliza un modelo lingüístico grande (LLM) para resumir y consultar novelas o relatos. Su objetivo es solucionar el problema de los métodos RAG convencionales, que solo pueden leer fragmentos del texto y no pueden localizar con precisión los fragmentos necesarios para obtener el contexto completo. Al importar un libro, se necesitan un poco más de tokens que la longitud total del texto para realizar un resumen; durante las consultas, ya que solo se necesita el contenido del resumen y parte del texto original, el número de tokens utilizado no será significativamente mayor que en los métodos RAG convencionales.

Antes de ejecutar el proyecto, debe colocar el contenido a resumir en "book.txt" y crear las carpetas "chapter", "chapter2", "summarize" y "summarize2". Antes de usar el programa, es necesario configurar la API en "api.py". Para garantizar que el contenido de salida cumpla con los requisitos, se recomienda utilizar Deepseek Coder v2 u otro LLM con capacidades lógicas similares. Estos modelos también pueden ayudar en el desarrollo y mantenimiento del proyecto. Los contenidos de diálogo de cada archivo del programa están disponibles en archivos .txt con el mismo nombre, excepto "api.py" que no utilizó asistencia de LLM en su desarrollo.

Los archivos del proyecto se han nombrado según su función. Al utilizar el programa, primero debe ejecutar "Split.py" (por defecto coincide con el carácter '------------'. Debe ajustarse según el carácter utilizado para dividir el texto en "book.txt") y "Summarize.py", para obtener un resumen de primer nivel de cada sección. "Connect1.py" se utiliza para conectar los contenidos de los resúmenes de primer nivel en secciones más largas, que luego son resumidos por "Summarize2.py" y se extraen las palabras clave. Una vez completado el resumen de segundo nivel, ejecute "Connect2.py" para obtener "summarize2.txt". Si no es necesario realizar un resumen de segundo nivel, ejecute "Connect.py" para obtener "summarize.txt".

"Search1.py" se utiliza para buscar contenido en los resúmenes de primer nivel. Si el modelo solicita obtener parte del texto original, se le enviará el contenido correspondiente y se imprimirá. Luego, el LLM responderá a la pregunta después de acceder al texto original proporcionado. "Search2.py" se utiliza para buscar contenido en los resúmenes de segundo nivel. Si el modelo solicita obtener el contenido del resumen de primer nivel, se le enviará el contenido correspondiente y se imprimirá. Los pasos siguientes son similares a los de "Search1.py".

El proyecto contiene versiones en varios idiomas, todas ellas traducidas mediante LLM. El repositorio solo incluye la versión en chino. Las demás versiones están empaquetadas en archivos comprimidos. La traducción incluye las instrucciones, los nombres de los archivos de los programas que se ejecutan (excepto la versión en chino, que utiliza nombres en inglés) y las sugerencias (incluyendo "api.py" y las sugerencias para crear archivos). Los demás archivos y carpetas siguen utilizando inglés. Además, para evitar que el LLM confunda las tareas durante la traducción, se ha eliminado la frase que solicita desarrollar un programa en Python del archivo que contiene las sugerencias. Si detecta algún error de traducción, puede modificarlo y enviarlo como una propuesta.

Resultados de prueba: Deepseek Coder v2 puede completar la tarea de resumen, pero en las pruebas de recuperación, cuando se le plantearon varios problemas, el modelo no solicitó obtener el contenido original y solo respondió basándose en el contenido resumido. Si tienen APIs de otros modelos que puedan probarse, también pueden dar sugerencias de modificación.  


النسخة العربية
يُستخدم هذا المشروع لاستدعاء LLM لإنشاء ملخصات واستفسارات عن الروايات أو النصوص القصصية. الهدف هو معالجة مشكلة أن طرق rag التقليدية لا يمكنها قراءة سوى مقاطع قصيرة من النص ولا تستطيع تحديد المقطع المطلوب للحصول على النص الأصلي بدقة. عند استيراد كتاب، يتطلب الأمر أكثر من عدد tokens الكامل للنص لإنشاء ملخص له، أما عند إجراء الاستفسار، فيستخدم عدد tokens أقل بشكل ملحوظ مقارنة بطرق rag التقليدية حيث لا يلزم إرسال سوى الملخص والمقطع الأصلي المحدد.

يجب وضع محتوى النص الذي سيتم تلخيصه في ملف "book.txt" وقم بإنشاء مجلدات "chapter"، "chapter2"، "summarize"، "summarize2" قبل التشغيل. ويجب أيضًا ضبط API في ملف "api.py" قبل الاستخدام. ولضمان أن يكون المحتوى الناتج مطابقًا للمتطلبات، يُنصح باستخدام Deepseek Coder v2 أو LLM آخر بمستوى قدرة منطقية مماثلة، ويمكن لهذه LLM المساعدة في تطوير وصيانة هذا المشروع. يتم الاحتفاظ بمحادثات ملفات البرنامج في ملفات txt ذات الاسم نفسه، ولم يُستخدم LLM في تطوير ملف "api.py".

تمت تسمية ملفات المشروع حسب وظائفها، ويجب تشغيل "Split.py" أولاً (يتوافق بشكل افتراضي مع رمز "------------") وقم ضبطه وفقًا للرمز المستخدم في فصل "book.txt"، ثم تشغيل "Summarize.py" للحصول على ملخصات من الدرجة الأولى لكل جزء. يتم استخدام "Connect1.py" لتوصيل محتوى ملخصات الدرجة الأولى لإنشاء مقاطع أطول، ثم يقوم "Summarize2.py" بإنشاء ملخصات من الدرجة الثانية واستخراج الكلمات الرئيسية. بعد الانتهاء من الملخصات من الدرجة الثانية، قم بتشغيل "Connect2.py" للحصول على ملف "summarize2.txt". إذا لم تكن هناك حاجة إلى ملخصات من الدرجة الثانية، فيجب تشغيل "Connect.py" للحصول على ملف "summarize.txt".

يُستخدم "Search1.py" للبحث عن محتوى في ملخصات الدرجة الأولى، وإذا طلب نموذج الحصول على جزء من النص الأصلي، فسيتم إرسال الجزء المحدد وتصفح النتائج، وبعد ذلك يقوم LLM بالرد على الأسئلة بناءً على النص الأصلي الذي تم الحصول عليه. يستخدم "Search2.py" للبحث عن محتوى في ملخصات الدرجة الثانية، وإذا طلب نموذج الحصول على محتوى ملخصات الدرجة الأولى، فسيتم إرسال الجزء المحدد وتصفح النتائج، وبعد ذلك تتم الخطوات التالية بنفس طريقة "Search1.py".

يشمل المشروع إصدارات بلغات مختلفة، حيث تم ترجمة جميعها باستخدام LLM. يحتوي الودائع على ملفات الإصدار باللغة الصينية فقط، بينما يتم ضغط إصدارات اللغات الأخرى. تشمل الترجمة: الوصف، أسماء ملفات البرنامج التي سيتم تنفيذها (باستثناء الإصدار باللغة الصينية حيث تستخدم الأسماء باللغة الإنجليزية)، والعبارات الدلالية (بما في ذلك "api.py" وكلمات تحذير إنشاء الملف). ولا تزال الملفات والمجلدات الأخرى تستخدم اللغة الإنجليزية. بالإضافة إلى ذلك، لمنع خلط المهام لدى LLM أثناء الترجمة، تم إزالة الجمل التي تتطلب كتابة برنامج بيثون من ملفات العبارات الدلالية. إذا لاحظت خطأً في الترجمة، يمكنك تعديله ومراجعته.

نتائج الاختبار: تمكن Deepseek Coder v2 من إنجاز مهمة تلخيص النص، لكن عند اختبار خاصية استرجاع المعلومات لمجموعة من الأسئلة، لم يطلب النّموذج الحصول على محتوى النص الأصلي في أي مرة، بل قام بالرد بناءً على محتوى التلخيص فقط. 

إذا كان لديكمAPIs لنماذج أخرى يمكن اختبارها بشكل أوسع، يمكنك أيضاً تقديم اقتراحات لتحسين هذا النّموذج.  




