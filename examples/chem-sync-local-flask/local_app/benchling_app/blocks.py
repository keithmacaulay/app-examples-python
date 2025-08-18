from benchling_sdk.models import (
    MarkdownUiBlock, 
    MarkdownUiBlockType, 
    ButtonUiBlock, 
    ButtonUiBlockType,
    SectionUiBlock,
    SectionUiBlockType,
    FileUploadUiBlock,
    FileUploadUiBlockType,
    TableUiBlock,
    TableUiBlockType,
    TableUiBlockDataFrameSource,
    TableUiBlockDataFrameSourceType,
    DropdownUiBlock,
    DropdownUiBlockType,
    DropdownMultiValueUiBlock,
    DropdownMultiValueUiBlockType,
    SelectorInputUiBlock,
    SelectorInputUiBlockType,
    SelectorInputMultiValueUiBlock,
    SelectorInputMultiValueUiBlockType,
    TextInputUiBlock,
    TextInputUiBlockType,
    SearchInputUiBlock,
    SearchInputUiBlockType,
    SearchInputMultiValueUiBlock,
    SearchInputMultiValueUiBlockType,   
    SearchInputUiBlockItemType,
    ChipUiBlock,
    ChipUiBlockType,
    MarkdownUiBlock,
    MarkdownUiBlockType,
    ButtonUiBlock,
    ButtonUiBlockType,
    SectionUiBlock,
    SectionUiBlockType,
)


blocks = [
    [
        MarkdownUiBlock(
            id="markdown_1",
            type=MarkdownUiBlockType.MARKDOWN,
            value="# 📜 Markdown UI Block",
        ),
        MarkdownUiBlock(
            id="markdown_1a",
            type=MarkdownUiBlockType.MARKDOWN,
            value="This is an example of a Markdown UI Block. For more on Markdown, see the description of Basic Syntax at [markdownguide.org](https://www.markdownguide.org/cheat-sheet/).\n # This is a level 1 header\n ## This is a level 2 header\n ### This is a level 3 header\n\n This is a paragraph with some **bold text**, *italic text* and ***bold italic text***.\n\n```text\nThis is a code block...\n...with two lines.\n```\n\nHere's an example image:\n\n ![This is an example image](data:image/png;base64,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)",
        ),
        MarkdownUiBlock(
            id="markdown_1b",
            type=MarkdownUiBlockType.MARKDOWN,
            value="### API Example\n```json\n{\n    \"id\": \"markdown_1\",\n    \"type\": \"MARKDOWN\",\n    \"value\": \"This is a *markdown* block\"\n}",
        ),
        MarkdownUiBlock(
            id="markdown_1c",
            type=MarkdownUiBlockType.MARKDOWN,
            value="### SDK Example\n```python\nfrom benchling_sdk.models import (\n    MarkdownUiBlock,\n    MarkdownUiBlockType,\n)\n\nMarkdownUiBlock(\n    id='markdown_1',\n    type=MarkdownUiBlockType.MARKDOWN,\n    value='This is a *Markdown* block',\n)",
        ),
        SectionUiBlock(
            id="nav_buttons_1",
            type=SectionUiBlockType.SECTION,
            children=[
                ButtonUiBlock(
                    id="prev_1",
                    text="< Prev",
                    type=ButtonUiBlockType.BUTTON,
                ),
                ButtonUiBlock(
                    id="next_1",
                    text="Next >",
                    type=ButtonUiBlockType.BUTTON,
                ),
            ]
        ),
    ],
    [
        MarkdownUiBlock(
            id="markdown_2",
            type=MarkdownUiBlockType.MARKDOWN,
            value="# 🔘 Button and Section UI Blocks",
        ),
        MarkdownUiBlock(
            id="markdown_2a",
            type=MarkdownUiBlockType.MARKDOWN,
            value="Here are some buttons:",
        ),
        ButtonUiBlock(
            id="button_1",
            text="Click me!",
            type=ButtonUiBlockType.BUTTON,
        ),
        ButtonUiBlock(
            id="button_2",
            text="You can't click me",
            type=ButtonUiBlockType.BUTTON,
            enabled=False,
        ),
        MarkdownUiBlock(
            id="markdown_2b",
            type=MarkdownUiBlockType.MARKDOWN,
            value="Here are some buttons within a section:",
        ),
        SectionUiBlock(
            id="section_2",
            type=SectionUiBlockType.SECTION,
            children=[
                ButtonUiBlock(
                    id="button_3",
                    text="Click me!",
                    type=ButtonUiBlockType.BUTTON,
                ),
                ButtonUiBlock(
                    id="button_4",
                    text="You can't click me",
                    enabled=False,
                    type=ButtonUiBlockType.BUTTON,
                ),
            ]
        ),
        MarkdownUiBlock(
            id="markdown_2c",
            type=MarkdownUiBlockType.MARKDOWN,
            value="### API Example\n```json\n{\n    \"id\": \"button_1\",\n    \"type\": \"BUTTON\",\n    \"text\": \"Click me!\"\n}\n\n{\n    \"id\": \"button_2\",\n    \"type\": \"BUTTON\",\n    \"text\": \"You can't click me\",\n    \"enabled\": false\n}\n\n{\n    \"id\": \"section_2\",\n    \"type\": \"SECTION\",\n    \"children\": [\n        {\n            \"id\": \"button_3\",\n            \"type\": \"BUTTON\",\n            \"text\": \"Click Me!\"\n        },\n        {\n            \"id\": \"button_4\",\n            \"type\": \"BUTTON\",\n            \"text\": \"You can't click me\",\n            \"enabled\": false\n        }\n    ]\n}",
        ),
        MarkdownUiBlock(
            id="markdown_2d",
            type=MarkdownUiBlockType.MARKDOWN,
            value="### SDK Example\n```python\nfrom benchling_sdk.models import (\n    ButtonUiBlock,\n    ButtonUiBlockType,\n)\n\nButtonUiBlock(\n    id='button_1',\n    type=ButtonUiBlockType.BUTTON,\n    text='Click me!',\n)\n\nButtonUiBlock(\n    id='button_2',\n    type=ButtonUiBlockType.BUTTON,\n    text='You can't click me',\n    enabled=False,\n)\n\nSectionUiBlock(\n    id='section_2',\n    type=SectionUiBlockType.SECTION,\n    children=[\n        ButtonUiBlock(\n            id='button_3',\n            type=ButtonUiBlockType.BUTTON,\n            text='Click Me!',\n        ),\n        ButtonUiBlock(\n            id='button_4',\n            type=ButtonUiBlockType.BUTTON,\n            text='You can't click me',\n            enabled=False,\n        ),\n    ],\n)",
        ),
        SectionUiBlock(
            id="nav_buttons_2",
            type=SectionUiBlockType.SECTION,
            children=[
                ButtonUiBlock(
                    id="prev_2",
                    text="< Prev",
                    type=ButtonUiBlockType.BUTTON,
                ),
                ButtonUiBlock(
                    id="next_2",
                    text="Next >",
                    type=ButtonUiBlockType.BUTTON,
                ),
            ]
        ),
    ],
    [
        MarkdownUiBlock(
            id="markdown_3",
            type=MarkdownUiBlockType.MARKDOWN,
            value="# ⌨️ Text Input UI Block",
        ),
        TextInputUiBlock(
            id="text_input_3",
            type=TextInputUiBlockType.TEXT_INPUT,
            placeholder="(Placeholder) Enter some text",
            label="(Label) Text Input 1",
        ),
        TextInputUiBlock(
            id="text_input_3a",
            type=TextInputUiBlockType.TEXT_INPUT,
            value="This is a disabled text block",
            label="(Label) Text Input 2",
            enabled=False,
        ),
        MarkdownUiBlock(
            id="markdown_3b",
            type=MarkdownUiBlockType.MARKDOWN,
            value="### API Example\n```json\n{\n    \"id\": \"text_input_1\",\n    \"type\": \"TEXT_INPUT\",\n    \"placeholder\": \"(Placeholder) Enter some text\",\n    \"label\": \"(Label) Text Input 1\"\n}\n\n{\n    \"id\": \"text_input_1a\",\n    \"type\": \"TEXT_INPUT\",\n    \"value\": \"This is a disabled text block\",\n    \"enabled\": false,\n    \"label\": \"(Label) Text Input 2\"\n}",
        ),
        MarkdownUiBlock(
            id="markdown_3c",
            type=MarkdownUiBlockType.MARKDOWN,
            value="### SDK Example\n```python\nfrom benchling_sdk.models import (\n    TextInputUiBlock,\n    TextInputUiBlockType,\n)\n\nTextInputUiBlock(\n    id='text_input_1',\n    type=TextInputUiBlockType.TEXT_INPUT,\n    placeholder='(Placeholder) Enter some text',\n    label='(Label) Text Input 1',\n)\n\nTextInputUiBlock(\n    id='text_input_1a',\n    type=TextInputUiBlockType.TEXT_INPUT,\n    value='This is a disabled text block',\n    enabled=False,\n    label='(Label) Text Input 2',\n)",
        ),
        SectionUiBlock(
            id="nav_buttons_3",
            type=SectionUiBlockType.SECTION,
            children=[
                ButtonUiBlock(
                    id="prev_3",
                    text="< Prev",
                    type=ButtonUiBlockType.BUTTON,
                ),
                ButtonUiBlock(
                    id="next_3",
                    text="Next >",
                    type=ButtonUiBlockType.BUTTON,
                ),
            ]
        ),
    ],
    [
        MarkdownUiBlock(
            id="markdown_4",
            type=MarkdownUiBlockType.MARKDOWN,
            value="# 🔽 Dropdown UI Blocks",
        ),
        DropdownUiBlock(
            id="dropdown_4",
            label="(Label) This is a single-select dropdown",
            dropdown_id="sfs_hB7LHTUNgY",
            type=DropdownUiBlockType.DROPDOWN,
        ),
        DropdownMultiValueUiBlock(
            id="dropdownmulti_4",
            label="(Label) This is a multi-select dropdown",
            dropdown_id="sfs_hB7LHTUNgY",
            type=DropdownMultiValueUiBlockType.DROPDOWN_MULTIVALUE,
        ),
        MarkdownUiBlock(
            id="markdown_4a",
            type=MarkdownUiBlockType.MARKDOWN,
            value="### API Examples\n```json\n{\n    \"id\": \"dropdown_1\",\n    \"label\": \"(Label) This is a single-select dropdown\",\n    \"type\": \"DROPDOWN\",\n    \"dropdownId\": \"sfs_abc123def\"\n}\n\n{\n    \"id\": \"dropdownmulti_1\",\n    \"label\": \"(Label) This is a multi-select dropdown\",\n    \"type\": \"DROPDOWN_MULTIVALUE\",\n    \"dropdownId\": \"sfs_abc123def\"\n}",
        ),
        MarkdownUiBlock(
            id="markdown_4b",
            type=MarkdownUiBlockType.MARKDOWN,
            value="### SDK Examples\n```python\n# Dropdown UI Block\nfrom benchling_sdk.models import (\n    DropdownUiBlock,\n    DropdownUiBlockType,\n)\n\nDropdownUiBlock(\n    id='dropdown_1',\n    type=DropdownUiBlockType.DROPDOWN,\n    label='(Label) This is a single-select dropdown',\n    dropdown_id='sfs_abc123def',\n)\n\n# Dropdown Multi-Value UI Block\nfrom benchling_sdk.models import (\n    DropdownMultiValueUiBlock,\n    DropdownMultiValueUiBlockType,\n)\n\nDropdownMultiValueUiBlock(\n    id='dropdownmulti_1',\n    type=DropdownMultiValueUiBlockType.DROPDOWN_MULTIVALUE,\n    label='(Label) This is a multi-select dropdown',\n    dropdown_id='sfs_abc123def',\n)",
        ),
        SectionUiBlock(
            id="nav_buttons_4",
            type=SectionUiBlockType.SECTION,
            children=[
                ButtonUiBlock(
                    id="prev_4",
                    text="< Prev",
                    type=ButtonUiBlockType.BUTTON,
                ),
                ButtonUiBlock(
                    id="next_4",
                    text="Next >",
                    type=ButtonUiBlockType.BUTTON,
                ),
            ]
        ),
    ],
    [
        MarkdownUiBlock(
            id="markdown_5",
            type=MarkdownUiBlockType.MARKDOWN,
            value="# 🔽 Selector UI Blocks",
        ),
        SelectorInputUiBlock(
            id="selector_5",
            label="(Label) This is a single-select selector",
            type=SelectorInputUiBlockType.SELECTOR_INPUT,
            options=["Carrot", "Potato", "Tomato", "Onion", "Garlic", "Lettuce", "Cucumber"],
        ),
        SelectorInputMultiValueUiBlock(
            id="selectormulti_5",
            label="(Label) This is a multi-select selector",
            type=SelectorInputMultiValueUiBlockType.SELECTOR_INPUT_MULTIVALUE,
            options=["Carrot", "Potato", "Tomato", "Onion", "Garlic", "Lettuce", "Cucumber"],
        ),
        MarkdownUiBlock(
            id="markdown_5a",
            type=MarkdownUiBlockType.MARKDOWN,
            value="### API Examples\n```json\n{\n    \"id\": \"selector_1\",\n    \"label\": \"(Label) This is a single-select selector\",\n    \"type\": \"SELECTOR_INPUT\",\n    \"options\": [\n        \"Carrot\",\n        \"Potato\",\n        \"Tomato\",\n        \"Onion\",\n        \"Garlic\",\n        \"Lettuce\",\n        \"Cucumber\"\n    ]\n}\n\n{\n    \"id\": \"selectormulti_1\",\n    \"label\": \"(Label) This is a multi-select selector\",\n    \"type\": \"SELECTOR_INPUT_MULTIVALUE\",\n    \"options\": [\n        \"Carrot\",\n        \"Potato\",\n        \"Tomato\",\n        \"Onion\",\n        \"Garlic\",\n        \"Lettuce\",\n        \"Cucumber\"\n    ]\n}",
        ),
        MarkdownUiBlock(
            id="markdown_5b",
            type=MarkdownUiBlockType.MARKDOWN,
            value="### SDK Examples\n```python\n# Selector UI Block\nfrom benchling_sdk.models import (\n    SelectorInputUiBlock,\n    SelectorInputUiBlockType,\n)\n\nSelectorInputUiBlock(\n    id='selector_1',\n    type=SelectorInputUiBlockType.SELECTOR_INPUT,\n    label='(Label) This is a single-select selector',\n    options=['Carrot', 'Potato', 'Tomato', 'Onion', 'Garlic', 'Lettuce', 'Cucumber'],\n)\n\n# Selector Multi-Value UI Block\nfrom benchling_sdk.models import (\n    SelectorInputMultiValueUiBlock,\n    SelectorInputMultiValueUiBlockType,\n)\n\nSelectorInputMultiValueUiBlock(\n    id='selectormulti_1',\n    type=SelectorInputMultiValueUiBlockType.SELECTOR_INPUT_MULTIVALUE,\n    label='(Label) This is a multi-select selector',\n    options=['Carrot', 'Potato', 'Tomato', 'Onion', 'Garlic', 'Lettuce', 'Cucumber'],\n)",
        ),
        SectionUiBlock(
            id="nav_buttons_5",
            type=SectionUiBlockType.SECTION,
            children=[
                ButtonUiBlock(
                    id="prev_5",
                    text="< Prev",
                    type=ButtonUiBlockType.BUTTON,
                ),
                ButtonUiBlock(
                    id="next_5",
                    text="Next >",
                    type=ButtonUiBlockType.BUTTON,
                ),
            ]
        ),
    ],
    [
        MarkdownUiBlock(
            id="markdown_6",
            type=MarkdownUiBlockType.MARKDOWN,
            value="# 🔎 Search Input UI Blocks",
        ),
        SearchInputUiBlock(
            id="search_6",
            type=SearchInputUiBlockType.SEARCH_INPUT,
            item_type=SearchInputUiBlockItemType.CUSTOM_ENTITY,
            label="(Label) Search for a custom entity",
            placeholder="(Placeholder) Search for a custom entity",
            schema_id="ts_g9Et54EA",
        ),
        SearchInputMultiValueUiBlock(
            id="searchmulti_6",
            type=SearchInputMultiValueUiBlockType.SEARCH_INPUT_MULTIVALUE,
            item_type=SearchInputUiBlockItemType.CUSTOM_ENTITY,
            label="(Label) Search for several custom entities",
            placeholder="(Placeholder) Search for several custom entities",
            schema_id="ts_g9Et54EA",
        ),
        MarkdownUiBlock(
            id="markdown_6a",
            type=MarkdownUiBlockType.MARKDOWN,
            value="### API Examples\n```json\n{\n    \"id\": \"search_1\",\n    \"label\": \"(Label) Search for a custom entity\",\n    \"type\": \"SEARCH_INPUT\",\n    \"itemType\": \"CUSTOM_ENTITY\",\n    \"schemaId\": \"ts_abc123def\",\n    \"placeholder\": \"(Placeholder) Search for a custom entity\"\n}\n\n{\n    \"id\": \"searchmulti_1\",\n    \"label\": \"(Label) Search for several custom entities\",\n    \"type\": \"SEARCH_INPUT_MULTIVALUE\",\n    \"itemType\": \"CUSTOM_ENTITY\",\n    \"schemaId\": \"ts_abc123def\",\n    \"placeholder\": \"(Placeholder) Search for several custom entities\"\n}",
        ),
        MarkdownUiBlock(
            id="markdown_6b",
            type=MarkdownUiBlockType.MARKDOWN,
            value="### SDK Examples\n```python\n#    Search Input UI Block\nfrom benchling_sdk.models import (\n    SearchInputUiBlock,\n    SearchInputUiBlockType,\n)\n\nSearchInputUiBlock(\n    id='search_1',\n    type=SearchInputUiBlockType.SEARCH_INPUT,\n    item_type=SearchInputUiBlockItemType.CUSTOM_ENTITY,\n    schema_id='ts_abc123def',\n    placeholder='(Placeholder) Search for a custom entity',\n)\n\n# Search Input Multi-Value UI Block\nfrom benchling_sdk.models import (\n    SearchInputMultiValueUiBlock,\n    SearchInputMultiValueUiBlockType,\n)\n\nSearchInputMultiValueUiBlock(\n    id='searchmulti_1',\n    type=SearchInputMultiValueUiBlockType.SEARCH_INPUT_MULTIVALUE,\n    item_type=SearchInputUiBlockItemType.CUSTOM_ENTITY,\n    schema_id='ts_abc123def',\n    placeholder='(Placeholder) Search for several custom entities',\n)",
        ),
        SectionUiBlock(
            id="nav_buttons_6",
            type=SectionUiBlockType.SECTION,
            children=[
                ButtonUiBlock(
                    id="prev_6",
                    text="< Prev",
                    type=ButtonUiBlockType.BUTTON,
                ),
                ButtonUiBlock(
                    id="next_6",
                    text="Next >",
                    type=ButtonUiBlockType.BUTTON,
                ),
            ]
        ),
    ],
    [
        MarkdownUiBlock(
            id="markdown_7",
            type=MarkdownUiBlockType.MARKDOWN,
            value="# 🥔 Chip UI Block",
        ),
        MarkdownUiBlock(
            id="markdown_7a",
            type=MarkdownUiBlockType.MARKDOWN,
            value="Here's an example of a chip - hover over it to see the metadata:",
        ),
        ChipUiBlock(
            id="chip_7",
            type=ChipUiBlockType.CHIP,
            value="mol_zHH2lZ9r",
        ),
        MarkdownUiBlock(
            id="markdown_7b",
            type=MarkdownUiBlockType.MARKDOWN,
            value="### API Examples\n```json\n{\n    \"id\": \"chip_1\",\n    \"type\": \"CHIP\",\n    \"value\": \"bfi_abc123def\"\n}",
        ),
        MarkdownUiBlock(
            id="markdown_7c",
            type=MarkdownUiBlockType.MARKDOWN,
            value="### SDK Examples\n```python\nfrom benchling_sdk.models import (\n    ChipUiBlock,\n    ChipUiBlockType,\n)\n\nChipUiBlock(\n    id='chip_1',\n    type=ChipUiBlockType.CHIP,\n    value='bfi_abc123def',\n)",
        ),
        SectionUiBlock(
            id="nav_buttons_7",
            type=SectionUiBlockType.SECTION,
            children=[
                ButtonUiBlock(
                    id="prev_7",
                    text="< Prev",
                    type=ButtonUiBlockType.BUTTON,
                ),
                ButtonUiBlock(
                    id="next_7",
                    text="Next >",
                    type=ButtonUiBlockType.BUTTON,
                ),
            ]
        ),
    ],
    [
        MarkdownUiBlock(
            id="markdown_8",
            type=MarkdownUiBlockType.MARKDOWN,
            value="# ⬆️ File Upload UI Block",
        ),
        FileUploadUiBlock(
            id="file_upload_8",
            type=FileUploadUiBlockType.FILE_UPLOAD,
            label="(Label) Upload a CSV file",
            required=False,
            file_types=["text/csv"],
            max_files=1,
        ),
        MarkdownUiBlock(
            id="markdown_8a",
            type=MarkdownUiBlockType.MARKDOWN,
            value="### API Example\n```json\n{\n    \"id\": \"file_upload_1\",\n    \"name\": \"(Label) Upload a file\",\n    \"type\": \"FILE_UPLOAD\",\n    \"required\": false,\n    \"fileTypes\": [\n        \"text/csv\"\n    ],\n    \"maxFiles\": 1\n}",
        ),
        MarkdownUiBlock(
            id="markdown_8b",
            type=MarkdownUiBlockType.MARKDOWN,
            value="### SDK Example\n```python\nfrom benchling_sdk.models import (\n    FileUploadUiBlock,\n    FileUploadUiBlockType,\n)\n\nFileUploadUiBlock(\n    id='file_upload_1',\n    type=FileUploadUiBlockType.FILE_UPLOAD,\n    label='(Label) Upload a file',\n    required=False,\n    file_types=['text/csv'],\n    max_files=1,\n)",
        ),
        SectionUiBlock(
            id="nav_buttons_8",
            type=SectionUiBlockType.SECTION,
            children=[
                ButtonUiBlock(
                    id="prev_8",
                    text="< Prev",
                    type=ButtonUiBlockType.BUTTON,
                ),
                ButtonUiBlock(
                    id="next_8",
                    text="Next >",
                    type=ButtonUiBlockType.BUTTON,
                ),
            ]
        ),
    ],
    [
        MarkdownUiBlock(
            id="markdown_9",
            type=MarkdownUiBlockType.MARKDOWN,
            value="# 🧮 Table UI Block",
        ),
            MarkdownUiBlock(
            id="markdown_9a",
            type=MarkdownUiBlockType.MARKDOWN,
            value="# 🧮 Table UI Block",
        ),
        TableUiBlock(
            id="table_9",
            type=TableUiBlockType.TABLE,
            name="(Name) Table 1",
            source=TableUiBlockDataFrameSource(
                type=TableUiBlockDataFrameSourceType.DATA_FRAME,
                data_frame_id="dset_VfaggSQYn52S",
            ),
        ),
        MarkdownUiBlock(
            id="markdown_9b",
            type=MarkdownUiBlockType.MARKDOWN,
            value="### API Example\n```json\n{\n    \"id\": \"table_1\",\n    \"name\": \"(Name) Table 1)\",\n    \"source\": {\n        \"datasetId\": \"dset_abc123def\"\n    },\n    \"type\": \"TABLE\"\n}",
        ),
        MarkdownUiBlock(
            id="markdown_9c",
            type=MarkdownUiBlockType.MARKDOWN,
            value="### SDK Example\n```python\nfrom benchling_sdk.models import (\n    TableUiBlock,\n    TableUiBlockType,\n    TableUiBlockDataFrameSource,\n    TableUiBlockDataFrameSourceType,\n)\n\nTableUiBlock(\n    id='table_1',\n    type=TableUiBlockType.TABLE,\n    name='(Name) Table 1',\n    source=TableUiBlockDataFrameSource(\n        type=TableUiBlockDataFrameSourceType.DATA_FRAME,\n        data_frame_id='dset_abc123def',\n    ),\n)",
        ),
        SectionUiBlock(
            id="nav_buttons_9",
            type=SectionUiBlockType.SECTION,
            children=[
                ButtonUiBlock(
                    id="prev_9",
                    text="< Prev",
                    type=ButtonUiBlockType.BUTTON,
                ),
            ]
        ),
    ],
]