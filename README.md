# ImageCutter
Little tool to crop specified areas in images and save them as jpg files.

## Examples
Examples and expected directories form are available in ImageCutter/data directory.

## XML Format
Example XML:
```
<annotation>
    <filename>test.jpg</filename>
    <object>
        <name>object_type</name>
        <bndbox>
            <xmin>1</xmin>
            <ymin>2</ymin>
            <xmax>3</xmax>
            <ymax>4</ymax>
        </bndbox>
    </object>
</annotation>
```
Original files include more fields, but as those are not necessary to crop out desired areas I do not parse them and do not include in this example.
