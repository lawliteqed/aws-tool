erb = ERB.new(IO.read("file"), nil, "-")
puts erb.result(binding)
