# Diagrams

System architecture is written in python and converted to images by [diagrams](https://diagrams.mingrammer.com/)
Seequence flow is written in a markup language and converted to images by [planttext](https://www.planttext.com/).

**Pre-requisites**

-   python3
-   pip
-   [graphviz](https://graphviz.org/download/)
-   [diagrams](https://github.com/mingrammer/diagrams#getting-started)

## Generate diagrams

### System architecture

1. Create a new python file under `system-architecture`.
1. Write the diagram in your favourite (aka VSCode \o/) editor.
1. Generate the image from your terminal:

```bash
# considering your current directory is the same as this README
cd system-architecture && python3 your-diagram-file-name.py
```

1. The diagram image should be present under the same of the python file.

### Sequence flow

1. Go to https://www.planttext.com/
1. Write the diagram in the editor.
1. Export as PNG and save under `sequence-flow`.
1. Create a file in `sequence-flow` directory.
1. Copy and paste the code from the web editor into the created file and save it.
