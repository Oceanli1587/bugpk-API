from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("bugpk-music")

@mcp.tool()
async def get_music_resource(id: str, media: str, type: str = "song") -> str:
    """
    调用bugpk音乐解析接口，获取音乐播放地址、歌词、封面
    Args:
        id: 歌曲资源ID，QQ音乐示例：000j2RXp4eG7Vt
        media: 音乐平台，tencent=QQ音乐，netease=网易云
        type: 资源类型，song歌曲 / mv MV / url播放链接，默认song
    """
    base_url = "https://api.bugpk.com/api/music"
    params = {"id": id, "media": media, "type": type}
    try:
        async with httpx.AsyncClient(timeout=15) as client:
            resp = await client.get(base_url, params=params)
            data = resp.json()
        return str(data)
    except Exception as e:
        return f"接口请求失败：{str(e)}"

if __name__ == "__main__":
    mcp.run()
