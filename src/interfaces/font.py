import os


class Font:
	def __init__(self, name: str, **sizes):
		name_type = type(name)
		if name_type != str:
			message = f"Font name must be str, not {name_type}"
			raise ValueError(message)
		self._name = name
		file_name = name.replace(" ", "_")
		file_name += ".ttf"
		self._file_name = file_name
		self.sizes = [sizes["normal"]]
		self.sizes += [sizes["large"]]
		self.sizes += [sizes["giant"]]
		for index in range(len(self.sizes)):
			pick = int(self.sizes[index])
			self.sizes[index] = pick
		self._normal_size = self.sizes[0]
		self._large_size = self.sizes[1]
		self._giant_size = self.sizes[2]

	@property
	def name(self) -> str:
		return self._name

	@property
	def file_name(self) -> str:
		return self._file_name

	@property
	def path(self) -> str:
		path_args = ["fonts", self.file_name]
		return os.sep.join(path_args)

	@property
	def normal_size(self) -> int:
		return self._normal_size

	@property
	def large_size(self) -> int:
		return self._large_size

	@property
	def giant_size(self) -> int:
		return self._giant_size
