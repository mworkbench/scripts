require 'open-uri'
require 'nokogiri'
require 'uri'

if ARGV.size < 2 then
    p "Usage: % #{$0}  prefix url"
    p "   save to prefix-*** in files in url"
    exit()
end

# 保存対象ファイルの拡張子
POSTFIX = ["jpeg", "jpg", "gif", "mp4", "webm", "qt"]


PREFIX = ARGV[0]
URL = ARGV[1]


def  isValidLink(str)
    return POSTFIX.any? {|p| str.downcase.end_with? p }
end

def link2filename(l)
    return File.basename(URI.parse(l).path)
end

p "Saving to #{PREFIX}-***"
p "URL is #{URL}"

_links = []
uri = URI.parse(URL)
html = open(URL) do |data|
  data.read
end
doc = Nokogiri::HTML.parse(html)
doc.css('a').each do |anchor|
    # a タグの href要素を抜き出す。URLは相対パス名。
    rel_path = anchor[:href]
    if ! rel_path.downcase.include? "mailto" then
         # 絶対パス名に変換して 追加
        _links.push uri.merge(rel_path).to_s
    end
end

# 保存対象ファイルのURL (絶対パス名)
LINKS = _links.select {|l| isValidLink l}


count = 0
saveCount = 0
LINKS.each do |l|
    p "#{count} of #{LINKS.size}"
    open(l) do |file|
        inFilename = PREFIX + "-" + link2filename(l)
        if  FileTest.file? inFilename then
            p "File  #{inFilename}  is already saved."
        else
            p "Saving #{inFilename}"
            open(inFilename, "w+b") do |out|
                out.write(file.read)
            end
            saveCount = saveCount + 1
            p "Just saved and waiting 3 seconds"
            sleep(3)
        end
    end
    count = count + 1
end

p "#{saveCount} files are saved."
