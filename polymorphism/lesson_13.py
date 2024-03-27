class InputTag:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def render(self):
        return f'<input type="{self.type}" value="{self.value}">'

    def __str__(self):
        return self.render()


tag = InputTag('submit', 'Save')
print(tag.render())  # <input type="submit" value="Save">


class LabelTag:
    def __init__(self, text, tag):
        self.text = text
        self.tag = tag

    def render(self):
        res = f'<label>\n   {self.text}\n   {self.tag.render()}\n</label>'
        return res


input_tag = InputTag('submit', 'Save')
label_tag = LabelTag('Press Submit', input_tag)
print(label_tag.render())
# <label>
#   Press Submit
#   <input type="submit" value="Save">
# </label>
