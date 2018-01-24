from peewee import *

database = MySQLDatabase('51jianet', **{'password': 'zkeys', 'user': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class DedeAddon17(BaseModel):
    aid = PrimaryKeyField()
    cqnx = CharField()
    cwqk = CharField()
    huxing = CharField(null=True)
    jfsj = CharField()
    junjia = CharField(null=True)
    jzmj = CharField()
    kfs = CharField()
    kpsj = CharField()
    leixing = CharField(null=True)
    lhl = CharField()
    louceng = CharField(null=True)
    lpdz = CharField()
    lpjj = CharField()
    lpjs = TextField(null=True)
    nativeplace = CharField()
    pt = TextField(null=True)
    redirecturl = CharField()
    rjl = CharField()
    templet = CharField()
    typeid = IntegerField(index=True)
    userip = CharField()
    wyf = CharField()
    wygs = CharField()
    xmdz = CharField()
    xmts = CharField()
    zdmj = CharField()
    zhs = CharField()
    zhuangtai = CharField(null=True)
    zshx = TextField(null=True)
    zxqk = CharField(null=True)

    class Meta:
        db_table = 'dede_addon17'

class DedeAddon1718(BaseModel):
    aid = PrimaryKeyField()
    cqnx = CharField(null=True)
    cwqk = CharField(null=True)
    hxt = TextField(null=True)
    junjia = CharField(null=True)
    jysj = CharField(null=True)
    kfs = CharField(null=True)
    kpsj = CharField(null=True)
    leixing = CharField(null=True)
    lhl = CharField(null=True)
    lpdz = CharField(null=True)
    lpjs = TextField(null=True)
    pt = TextField(null=True)
    qx = CharField(null=True)
    rjl = CharField(null=True)
    sldz = CharField(null=True)
    templet = CharField(null=True)
    typeid = IntegerField(index=True, null=True)
    userip = TextField(null=True)
    wyf = CharField(null=True)
    wygs = CharField(null=True)
    xmts = CharField(null=True)
    zdmj = CharField(null=True)
    zhs = CharField(null=True)
    zlhx = CharField(null=True)
    zxzk = CharField(null=True)

    class Meta:
        db_table = 'dede_addon1718'

class DedeAddon19(BaseModel):
    aid = PrimaryKeyField()
    cqnx = CharField()
    cwqk = CharField()
    huxing = CharField(null=True)
    jfsj = CharField()
    junjia = CharField(null=True)
    jzmj = CharField()
    kfs = CharField()
    kpsj = CharField()
    leixing = CharField(null=True)
    lhl = CharField()
    louceng = CharField(null=True)
    lpdz = CharField()
    lpjj = CharField()
    lpjs = TextField(null=True)
    pt = TextField(null=True)
    qx = CharField(null=True)
    redirecturl = CharField()
    rjl = CharField()
    templet = CharField()
    typeid = IntegerField(index=True)
    userip = CharField()
    wyf = CharField()
    wygs = CharField()
    xmdz = CharField()
    xmts = CharField()
    zdmj = CharField()
    zhs = CharField()
    zhuangtai = CharField(null=True)
    zshx = TextField(null=True)
    zxqk = CharField(null=True)

    class Meta:
        db_table = 'dede_addon19'

class DedeAddon20(BaseModel):
    aid = PrimaryKeyField()
    cqnx = CharField()
    cwqk = CharField()
    huxing = CharField(null=True)
    jfsj = CharField()
    junjia = CharField(null=True)
    jzlb = CharField(null=True)
    jzmj = CharField()
    kfs = CharField()
    kpsj = CharField()
    leixing = CharField(null=True)
    lhl = CharField()
    louceng = CharField(null=True)
    lpdz = CharField()
    lpjj = CharField()
    lpjs = TextField(null=True)
    pt = TextField(null=True)
    qx = CharField(null=True)
    redirecturl = CharField()
    rjl = CharField()
    templet = CharField()
    typeid = IntegerField(index=True)
    userip = CharField()
    wyf = CharField()
    wygs = CharField()
    xmdz = CharField()
    xmts = CharField()
    zdmj = CharField()
    zhs = CharField()
    zhuangtai = CharField(null=True)
    zshx = TextField(null=True)
    zxqk = CharField(null=True)

    class Meta:
        db_table = 'dede_addon20'

class DedeAddon21(BaseModel):
    aid = PrimaryKeyField()
    cqnx = CharField()
    cwqk = CharField()
    hxt = TextField(null=True)
    jsmj = CharField()
    junjia = CharField()
    jysj = CharField()
    kfs = CharField()
    kpsj = CharField()
    leixing = CharField()
    lhl = CharField()
    lpdz = CharField()
    lpjs = TextField(null=True)
    pt = TextField(null=True)
    qx = CharField()
    redirecturl = CharField()
    rjl = CharField()
    sldz = CharField()
    templet = CharField()
    typeid = IntegerField(index=True)
    userip = CharField()
    wyf = CharField()
    wygs = CharField()
    xmts = CharField()
    zdmj = CharField()
    zhs = CharField()
    zlhx = CharField()
    zxzk = CharField()

    class Meta:
        db_table = 'dede_addon21'

class DedeAddonarticle(BaseModel):
    aid = PrimaryKeyField()
    body = TextField(null=True)
    redirecturl = CharField()
    templet = CharField()
    typeid = IntegerField(index=True)
    userip = CharField()

    class Meta:
        db_table = 'dede_addonarticle'

class DedeAddonimages(BaseModel):
    aid = PrimaryKeyField()
    body = TextField(null=True)
    col = IntegerField()
    ddmaxwidth = IntegerField()
    imgurls = TextField(null=True)
    isrm = IntegerField()
    maxwidth = IntegerField()
    pagepicnum = IntegerField()
    pagestyle = IntegerField()
    redirecturl = CharField()
    row = IntegerField()
    templet = CharField()
    typeid = IntegerField(index=True)
    userip = CharField()

    class Meta:
        db_table = 'dede_addonimages'

class DedeAddoninfos(BaseModel):
    address = CharField()
    aid = PrimaryKeyField()
    arcrank = IntegerField()
    badpost = IntegerField()
    body = TextField(null=True)
    channel = IntegerField()
    click = IntegerField()
    email = CharField()
    endtime = IntegerField()
    flag = CharField(null=True)
    goodpost = IntegerField()
    infotype = CharField()
    lastpost = IntegerField()
    linkman = CharField()
    litpic = CharField()
    mid = IntegerField()
    nativeplace = IntegerField()
    scores = IntegerField()
    senddate = IntegerField()
    tel = CharField()
    title = CharField()
    typeid = IntegerField()
    userip = CharField()

    class Meta:
        db_table = 'dede_addoninfos'
        indexes = (
            (('channel', 'arcrank', 'mid', 'click', 'title', 'litpic', 'senddate', 'flag', 'endtime'), False),
            (('typeid', 'nativeplace', 'infotype'), False),
        )

class DedeAddonshop(BaseModel):
    aid = PrimaryKeyField()
    body = TextField(null=True)
    brand = CharField()
    infotype = CharField()
    price = FloatField()
    redirecturl = CharField()
    templet = CharField()
    trueprice = FloatField()
    typeid = IntegerField(index=True)
    units = CharField()
    uptime = IntegerField()
    userip = CharField()
    vocation = CharField()

    class Meta:
        db_table = 'dede_addonshop'

class DedeAddonsoft(BaseModel):
    accredit = CharField()
    aid = PrimaryKeyField()
    daccess = IntegerField()
    filetype = CharField()
    introduce = TextField(null=True)
    language = CharField()
    needmoney = IntegerField()
    officialdemo = CharField(db_column='officialDemo')
    officialurl = CharField(db_column='officialUrl')
    os = CharField()
    redirecturl = CharField()
    softlinks = TextField(null=True)
    softrank = IntegerField()
    softsize = CharField()
    softtype = CharField()
    templet = CharField()
    typeid = IntegerField(index=True)
    userip = CharField()

    class Meta:
        db_table = 'dede_addonsoft'

class DedeAddonspec(BaseModel):
    aid = PrimaryKeyField()
    note = TextField(null=True)
    redirecturl = CharField()
    templet = CharField()
    typeid = IntegerField(index=True)
    userip = CharField()

    class Meta:
        db_table = 'dede_addonspec'

class DedeAdmin(BaseModel):
    email = CharField()
    loginip = CharField()
    logintime = IntegerField()
    pwd = CharField()
    tname = CharField()
    typeid = TextField(null=True)
    uname = CharField()
    userid = CharField()
    usertype = FloatField(null=True)

    class Meta:
        db_table = 'dede_admin'

class DedeAdmintype(BaseModel):
    purviews = TextField(null=True)
    rank = FloatField(primary_key=True)
    system = IntegerField()
    typename = CharField()

    class Meta:
        db_table = 'dede_admintype'

class DedeAdvancedsearch(BaseModel):
    addonfields = TextField(null=True)
    addontable = CharField(null=True)
    forms = TextField(null=True)
    mainfields = TextField(null=True)
    maintable = CharField()
    mid = IntegerField(unique=True)
    template = CharField()

    class Meta:
        db_table = 'dede_advancedsearch'
        primary_key = False

class DedeArcatt(BaseModel):
    att = CharField(primary_key=True)
    attname = CharField()
    sortid = IntegerField()

    class Meta:
        db_table = 'dede_arcatt'

class DedeArccache(BaseModel):
    cachedata = TextField(null=True)
    md5hash = CharField(primary_key=True)
    uptime = IntegerField()

    class Meta:
        db_table = 'dede_arccache'

class DedeArchives(BaseModel):
    arcrank = IntegerField()
    badpost = IntegerField()
    channel = IntegerField()
    click = IntegerField()
    color = CharField()
    description = CharField()
    dutyadmin = IntegerField()
    filename = CharField()
    flag = CharField(null=True)
    goodpost = IntegerField()
    ismake = IntegerField()
    keywords = CharField()
    lastpost = IntegerField()
    litpic = CharField()
    mid = IntegerField()
    money = IntegerField()
    mtype = IntegerField()
    notpost = IntegerField()
    pubdate = IntegerField()
    scores = IntegerField()
    senddate = IntegerField()
    shorttitle = CharField()
    sortrank = IntegerField(index=True)
    source = CharField()
    tackid = IntegerField()
    title = CharField()
    typeid = IntegerField()
    typeid2 = CharField()
    voteid = IntegerField()
    weight = IntegerField()
    writer = CharField()

    class Meta:
        db_table = 'dede_archives'
        indexes = (
            (('arcrank', 'typeid', 'channel', 'flag', 'mid'), False),
            (('lastpost', 'scores', 'goodpost', 'badpost', 'notpost'), False),
        )

class DedeArcmulti(BaseModel):
    addfieldssql = CharField(db_column='addfieldsSql', null=True)
    addfieldssqljoin = CharField(db_column='addfieldsSqlJoin', null=True)
    arcids = TextField()
    attstr = TextField(null=True)
    innertext = CharField()
    ordersql = CharField(null=True)
    pagesize = IntegerField()
    tagid = CharField()
    uptime = IntegerField()

    class Meta:
        db_table = 'dede_arcmulti'

class DedeArcrank(BaseModel):
    adminrank = IntegerField()
    membername = CharField()
    money = IntegerField()
    purviews = TextField(null=True)
    rank = IntegerField()
    scores = IntegerField()

    class Meta:
        db_table = 'dede_arcrank'

class DedeArctiny(BaseModel):
    arcrank = IntegerField()
    channel = IntegerField()
    mid = IntegerField()
    senddate = IntegerField()
    sortrank = IntegerField(index=True)
    typeid = IntegerField()
    typeid2 = CharField()

    class Meta:
        db_table = 'dede_arctiny'
        indexes = (
            (('typeid', 'arcrank', 'sortrank'), False),
        )

class DedeArctype(BaseModel):
    channeltype = IntegerField(null=True)
    content = TextField(null=True)
    corank = IntegerField()
    cross = IntegerField()
    crossid = TextField(null=True)
    defaultname = CharField()
    description = CharField()
    isdefault = IntegerField()
    ishidden = IntegerField()
    ispart = IntegerField()
    issend = IntegerField()
    keywords = CharField()
    maxpage = IntegerField()
    modname = CharField()
    moresite = IntegerField()
    namerule = CharField()
    namerule2 = CharField()
    reid = IntegerField()
    seotitle = CharField()
    sitepath = CharField()
    siteurl = CharField()
    smalltypes = TextField(null=True)
    sortrank = IntegerField(index=True)
    temparticle = CharField()
    tempindex = CharField()
    templist = CharField()
    topid = IntegerField()
    typedir = CharField()
    typename = CharField()

    class Meta:
        db_table = 'dede_arctype'
        indexes = (
            (('reid', 'isdefault', 'channeltype', 'ispart', 'corank', 'topid', 'ishidden'), False),
        )

class DedeArea(BaseModel):
    disorder = IntegerField()
    name = CharField()
    reid = IntegerField()

    class Meta:
        db_table = 'dede_area'

class DedeChanneltype(BaseModel):
    addcon = CharField()
    addtable = CharField()
    allfields = TextField(null=True)
    arcsta = IntegerField()
    dfcid = IntegerField()
    editcon = CharField()
    fieldset = TextField(null=True)
    isdefault = IntegerField()
    issend = IntegerField()
    isshow = IntegerField()
    issystem = IntegerField()
    listfields = TextField(null=True)
    maintable = CharField()
    mancon = CharField()
    needdes = IntegerField()
    needpic = IntegerField()
    nid = CharField()
    onlyone = IntegerField()
    sendrank = IntegerField()
    titlename = CharField()
    typename = CharField()
    useraddcon = CharField()
    usereditcon = CharField()
    usermancon = CharField()
    usertype = CharField()

    class Meta:
        db_table = 'dede_channeltype'
        indexes = (
            (('nid', 'isshow', 'arcsta', 'sendrank'), False),
        )

class DedeCoHtmls(BaseModel):
    aid = PrimaryKeyField()
    dtime = IntegerField()
    isdown = IntegerField()
    isexport = IntegerField()
    litpic = CharField()
    nid = IntegerField(index=True)
    result = TextField(null=True)
    title = CharField()
    typeid = IntegerField()
    url = CharField()

    class Meta:
        db_table = 'dede_co_htmls'
        indexes = (
            (('typeid', 'title', 'url', 'dtime', 'isdown', 'isexport'), False),
        )

class DedeCoMediaurls(BaseModel):
    hash = CharField(index=True)
    nid = IntegerField()
    tofile = CharField()

    class Meta:
        db_table = 'dede_co_mediaurls'
        primary_key = False

class DedeCoNote(BaseModel):
    channelid = IntegerField()
    cotime = IntegerField()
    isok = IntegerField()
    itemconfig = TextField(null=True)
    listconfig = TextField(null=True)
    nid = PrimaryKeyField()
    notename = CharField()
    pnum = IntegerField()
    sourcelang = CharField()
    uptime = IntegerField()
    usemore = IntegerField()

    class Meta:
        db_table = 'dede_co_note'
        indexes = (
            (('isok', 'channelid', 'cotime'), False),
        )

class DedeCoOnepage(BaseModel):
    issource = IntegerField()
    lang = CharField()
    rule = TextField(null=True)
    title = CharField()
    url = CharField(index=True)

    class Meta:
        db_table = 'dede_co_onepage'

class DedeCoUrls(BaseModel):
    hash = CharField()
    nid = IntegerField()

    class Meta:
        db_table = 'dede_co_urls'

class DedeDiyforms(BaseModel):
    diyid = PrimaryKeyField()
    info = TextField(null=True)
    listtemplate = CharField()
    name = CharField()
    posttemplate = CharField()
    public = IntegerField()
    table = CharField()
    viewtemplate = CharField()

    class Meta:
        db_table = 'dede_diyforms'

class DedeDlLog(BaseModel):
    dltime = IntegerField(index=True)
    dtype = CharField()
    ip = CharField()
    lang = CharField()
    referrer = CharField()
    user_agent = CharField()

    class Meta:
        db_table = 'dede_dl_log'
        indexes = (
            (('ip', 'dltime'), False),
        )

class DedeDownloads(BaseModel):
    downloads = IntegerField()
    hash = CharField(primary_key=True)
    id = IntegerField()

    class Meta:
        db_table = 'dede_downloads'

class DedeErradd(BaseModel):
    aid = IntegerField()
    errtxt = TextField(null=True)
    id = IntegerField(index=True)
    mid = IntegerField(null=True)
    oktxt = TextField(null=True)
    sendtime = IntegerField()
    title = CharField()
    type = IntegerField()

    class Meta:
        db_table = 'dede_erradd'
        primary_key = False

class DedeFeedback(BaseModel):
    aid = IntegerField()
    arctitle = CharField()
    bad = IntegerField()
    dtime = IntegerField()
    face = IntegerField()
    ftype = CharField()
    good = IntegerField()
    ip = CharField()
    ischeck = IntegerField()
    mid = IntegerField()
    msg = TextField(null=True)
    typeid = IntegerField()
    username = CharField()

    class Meta:
        db_table = 'dede_feedback'
        indexes = (
            (('aid', 'ischeck', 'mid'), False),
        )

class DedeFlink(BaseModel):
    dtime = IntegerField()
    email = CharField()
    ischeck = IntegerField()
    logo = CharField()
    msg = CharField()
    sortrank = IntegerField()
    typeid = IntegerField()
    url = CharField()
    webname = CharField()

    class Meta:
        db_table = 'dede_flink'

class DedeFlinktype(BaseModel):
    typename = CharField()

    class Meta:
        db_table = 'dede_flinktype'

class DedeFreelist(BaseModel):
    aid = PrimaryKeyField()
    click = IntegerField()
    defaultpage = CharField()
    description = CharField()
    edtime = IntegerField()
    keywords = CharField()
    listdir = CharField()
    listtag = TextField(null=True)
    maxpage = IntegerField()
    namerule = CharField()
    nodefault = IntegerField()
    templet = CharField()
    title = CharField()

    class Meta:
        db_table = 'dede_freelist'

class DedeHomepageset(BaseModel):
    position = CharField()
    showmod = IntegerField()
    templet = CharField()

    class Meta:
        db_table = 'dede_homepageset'
        primary_key = False

class DedeKeywords(BaseModel):
    aid = PrimaryKeyField()
    keyword = CharField()
    rank = IntegerField()
    rpurl = CharField()
    sta = IntegerField()

    class Meta:
        db_table = 'dede_keywords'
        indexes = (
            (('keyword', 'rank', 'sta'), False),
        )

class DedeLog(BaseModel):
    adminid = IntegerField()
    cip = CharField()
    dtime = IntegerField()
    filename = CharField()
    lid = PrimaryKeyField()
    method = CharField()
    query = CharField()

    class Meta:
        db_table = 'dede_log'

class DedeMember(BaseModel):
    checkmail = IntegerField()
    email = CharField()
    exptime = IntegerField()
    face = CharField()
    joinip = CharField()
    jointime = IntegerField()
    loginip = CharField()
    logintime = IntegerField(index=True)
    matt = IntegerField()
    mid = PrimaryKeyField()
    money = IntegerField()
    mtype = CharField()
    pwd = CharField()
    rank = IntegerField()
    safeanswer = CharField()
    safequestion = IntegerField()
    scores = IntegerField()
    sex = CharField()
    spacesta = IntegerField()
    uname = CharField()
    uptime = IntegerField()
    userid = CharField()

    class Meta:
        db_table = 'dede_member'
        indexes = (
            (('userid', 'sex'), False),
        )

class DedeMemberCompany(BaseModel):
    address = CharField()
    checked = IntegerField()
    comface = CharField()
    company = CharField()
    cosize = IntegerField()
    email = CharField()
    fax = CharField()
    introduce = TextField(null=True)
    linkman = CharField()
    mid = PrimaryKeyField()
    mobile = CharField()
    place = IntegerField()
    product = CharField()
    tel = CharField()
    uptime = IntegerField()
    url = CharField()
    vocation = IntegerField()

    class Meta:
        db_table = 'dede_member_company'

class DedeMemberFeed(BaseModel):
    aid = IntegerField()
    dtime = IntegerField()
    fid = PrimaryKeyField()
    ischeck = IntegerField()
    mid = IntegerField()
    note = CharField()
    title = CharField()
    type = CharField()
    uname = CharField()
    userid = CharField()

    class Meta:
        db_table = 'dede_member_feed'

class DedeMemberFlink(BaseModel):
    aid = PrimaryKeyField()
    mid = IntegerField()
    title = CharField()
    url = CharField()

    class Meta:
        db_table = 'dede_member_flink'

class DedeMemberFriends(BaseModel):
    addtime = IntegerField()
    description = CharField(null=True)
    fid = IntegerField()
    floginid = CharField()
    ftype = IntegerField()
    funame = CharField()
    groupid = IntegerField()
    mid = IntegerField()

    class Meta:
        db_table = 'dede_member_friends'
        indexes = (
            (('fid', 'mid'), False),
        )

class DedeMemberGroup(BaseModel):
    groupname = CharField()
    mid = IntegerField()

    class Meta:
        db_table = 'dede_member_group'

class DedeMemberGuestbook(BaseModel):
    aid = PrimaryKeyField()
    dtime = IntegerField()
    email = CharField()
    gid = CharField()
    ip = CharField()
    mid = IntegerField(index=True)
    msg = TextField(null=True)
    qq = CharField()
    tel = CharField()
    title = CharField()
    uname = CharField()

    class Meta:
        db_table = 'dede_member_guestbook'

class DedeMemberModel(BaseModel):
    description = CharField()
    info = TextField()
    issystem = IntegerField()
    name = CharField()
    state = IntegerField()
    table = CharField()

    class Meta:
        db_table = 'dede_member_model'

class DedeMemberMsg(BaseModel):
    dtime = IntegerField()
    ip = CharField()
    ischeck = IntegerField()
    mid = IntegerField()
    msg = TextField(null=True)
    userid = CharField()

    class Meta:
        db_table = 'dede_member_msg'
        indexes = (
            (('ischeck', 'mid'), False),
        )

class DedeMemberOperation(BaseModel):
    aid = PrimaryKeyField()
    buyid = CharField(index=True)
    mid = IntegerField()
    money = IntegerField()
    mtime = IntegerField()
    oldinfo = CharField()
    pid = IntegerField()
    pname = CharField()
    product = CharField()
    sta = IntegerField()

    class Meta:
        db_table = 'dede_member_operation'
        indexes = (
            (('pid', 'mid', 'sta'), False),
        )

class DedeMemberPerson(BaseModel):
    address = CharField()
    birthday = DateField()
    blood = IntegerField()
    bodytype = IntegerField()
    datingtype = IntegerField()
    drink = IntegerField()
    education = IntegerField()
    height = IntegerField()
    house = IntegerField()
    income = IntegerField()
    language = CharField(null=True)
    lovemsg = CharField()
    marital = IntegerField()
    mid = PrimaryKeyField()
    mobile = CharField()
    msn = CharField()
    nature = CharField(null=True)
    oldplace = IntegerField()
    onlynet = IntegerField()
    place = IntegerField()
    qq = CharField()
    sex = CharField()
    smoke = IntegerField()
    star = IntegerField()
    tel = CharField()
    uname = CharField()
    uptime = IntegerField()
    vocation = IntegerField()

    class Meta:
        db_table = 'dede_member_person'

class DedeMemberPms(BaseModel):
    floginid = CharField()
    folder = CharField(null=True)
    fromid = IntegerField()
    hasview = IntegerField()
    isadmin = IntegerField()
    message = TextField(null=True)
    sendtime = IntegerField(index=True)
    subject = CharField()
    toid = IntegerField()
    tologinid = CharField()
    writetime = IntegerField()

    class Meta:
        db_table = 'dede_member_pms'

class DedeMemberSnsmsg(BaseModel):
    mid = IntegerField()
    msg = CharField()
    sendtime = IntegerField()
    userid = CharField()

    class Meta:
        db_table = 'dede_member_snsmsg'

class DedeMemberSpace(BaseModel):
    matt = IntegerField()
    mid = PrimaryKeyField()
    pagesize = IntegerField()
    sign = CharField()
    spacelogo = CharField()
    spacename = CharField()
    spacenews = TextField(null=True)
    spacestyle = CharField()

    class Meta:
        db_table = 'dede_member_space'

class DedeMemberStow(BaseModel):
    addtime = IntegerField()
    aid = IntegerField()
    mid = IntegerField(index=True)
    title = CharField()
    type = CharField(null=True)

    class Meta:
        db_table = 'dede_member_stow'

class DedeMemberStowtype(BaseModel):
    indexname = CharField()
    indexurl = CharField()
    stowname = CharField(primary_key=True)

    class Meta:
        db_table = 'dede_member_stowtype'

class DedeMemberTj(BaseModel):
    album = IntegerField()
    archives = IntegerField()
    article = IntegerField()
    feedback = IntegerField()
    friend = IntegerField()
    homecount = IntegerField()
    info = IntegerField()
    mid = PrimaryKeyField()
    pagecount = IntegerField()
    shop = IntegerField()
    soft = IntegerField()
    stow = IntegerField()

    class Meta:
        db_table = 'dede_member_tj'

class DedeMemberType(BaseModel):
    aid = PrimaryKeyField()
    exptime = IntegerField()
    money = IntegerField()
    pname = CharField()
    rank = IntegerField()

    class Meta:
        db_table = 'dede_member_type'

class DedeMemberVhistory(BaseModel):
    count = IntegerField()
    loginid = CharField()
    mid = IntegerField()
    vid = IntegerField()
    vip = CharField()
    vloginid = CharField()
    vtime = IntegerField(index=True)

    class Meta:
        db_table = 'dede_member_vhistory'
        indexes = (
            (('mid', 'vid'), False),
        )

class DedeMoneycardRecord(BaseModel):
    aid = PrimaryKeyField()
    cardid = CharField(index=True)
    ctid = IntegerField(index=True)
    isexp = IntegerField()
    money = IntegerField()
    mtime = IntegerField()
    num = IntegerField()
    uid = IntegerField(index=True)
    utime = IntegerField()

    class Meta:
        db_table = 'dede_moneycard_record'

class DedeMoneycardType(BaseModel):
    money = IntegerField()
    num = IntegerField()
    pname = CharField()
    tid = PrimaryKeyField()

    class Meta:
        db_table = 'dede_moneycard_type'

class DedeMtypes(BaseModel):
    channelid = IntegerField()
    mid = IntegerField()
    mtypeid = PrimaryKeyField()
    mtypename = CharField()

    class Meta:
        db_table = 'dede_mtypes'

class DedeMultiservConfig(BaseModel):
    remoteupurl = TextField(db_column='remoteupUrl')
    remoteuploads = PrimaryKeyField()
    rminfo = TextField(null=True)
    servinfo = TextField(null=True)

    class Meta:
        db_table = 'dede_multiserv_config'

class DedeMyad(BaseModel):
    adname = CharField()
    aid = PrimaryKeyField()
    clsid = IntegerField()
    endtime = IntegerField()
    expbody = TextField(null=True)
    normbody = TextField(null=True)
    starttime = IntegerField()
    tagname = CharField()
    timeset = IntegerField()
    typeid = IntegerField()

    class Meta:
        db_table = 'dede_myad'
        indexes = (
            (('tagname', 'typeid', 'timeset', 'endtime', 'starttime'), False),
        )

class DedeMyadtype(BaseModel):
    typename = CharField()

    class Meta:
        db_table = 'dede_myadtype'

class DedeMytag(BaseModel):
    aid = PrimaryKeyField()
    endtime = IntegerField()
    expbody = TextField(null=True)
    normbody = TextField(null=True)
    starttime = IntegerField()
    tagname = CharField()
    timeset = IntegerField()
    typeid = IntegerField()

    class Meta:
        db_table = 'dede_mytag'
        indexes = (
            (('tagname', 'typeid', 'timeset', 'endtime', 'starttime'), False),
        )

class DedePayment(BaseModel):
    cod = IntegerField()
    code = CharField(unique=True)
    config = TextField()
    description = TextField()
    enabled = IntegerField()
    fee = CharField()
    name = CharField()
    online = IntegerField()
    rank = IntegerField()

    class Meta:
        db_table = 'dede_payment'

class DedePlus(BaseModel):
    aid = PrimaryKeyField()
    filelist = TextField(null=True)
    isshow = IntegerField()
    mainurl = CharField()
    menustring = CharField()
    plusname = CharField()
    writer = CharField()

    class Meta:
        db_table = 'dede_plus'

class DedePlusSeoinfo(BaseModel):
    alexa_area_num = CharField(null=True)
    alexa_num = CharField(null=True)
    baidu_count = CharField(null=True)
    create_time = IntegerField(null=True)
    haosou360_count = CharField(null=True)
    sogou_count = CharField(null=True)

    class Meta:
        db_table = 'dede_plus_seoinfo'

class DedePurview(BaseModel):
    mid = IntegerField(null=True)
    pkey = CharField(index=True)
    pvalue = TextField()
    rank = IntegerField(null=True)
    typeid = IntegerField(null=True)

    class Meta:
        db_table = 'dede_purview'
        primary_key = False

class DedePwdTmp(BaseModel):
    mailtime = IntegerField()
    membername = CharField()
    mid = PrimaryKeyField()
    pwd = CharField()

    class Meta:
        db_table = 'dede_pwd_tmp'

class DedeRatings(BaseModel):
    id = CharField(primary_key=True)
    total_value = IntegerField()
    total_votes = IntegerField()
    used_ips = TextField(null=True)

    class Meta:
        db_table = 'dede_ratings'

class DedeScores(BaseModel):
    icon = IntegerField(null=True)
    integral = IntegerField(index=True)
    isdefault = IntegerField()
    titles = CharField()

    class Meta:
        db_table = 'dede_scores'

class DedeSearchCache(BaseModel):
    hash = CharField(primary_key=True)
    ids = TextField(null=True)
    lasttime = IntegerField()
    rsnum = IntegerField()

    class Meta:
        db_table = 'dede_search_cache'

class DedeSearchKeywords(BaseModel):
    aid = PrimaryKeyField()
    channelid = IntegerField()
    count = IntegerField()
    keyword = CharField()
    lasttime = IntegerField()
    result = IntegerField()
    spwords = CharField()
    typeid = IntegerField()

    class Meta:
        db_table = 'dede_search_keywords'

class DedeSgpage(BaseModel):
    aid = PrimaryKeyField()
    body = TextField(null=True)
    description = CharField()
    filename = CharField()
    ismake = IntegerField()
    keywords = CharField()
    likeid = CharField(index=True)
    template = CharField()
    title = CharField()
    uptime = IntegerField()

    class Meta:
        db_table = 'dede_sgpage'
        indexes = (
            (('ismake', 'uptime'), False),
        )

class DedeShopsDelivery(BaseModel):
    des = CharField(null=True)
    dname = CharField()
    orders = IntegerField(index=True)
    pid = PrimaryKeyField()
    price = FloatField()

    class Meta:
        db_table = 'dede_shops_delivery'

class DedeShopsOrders(BaseModel):
    cartcount = IntegerField()
    dprice = FloatField()
    ip = CharField()
    oid = CharField(index=True)
    paytype = IntegerField()
    pid = IntegerField()
    price = FloatField()
    pricecount = FloatField(db_column='priceCount')
    state = IntegerField()
    stime = IntegerField(index=True)
    userid = IntegerField(index=True)

    class Meta:
        db_table = 'dede_shops_orders'
        primary_key = False

class DedeShopsProducts(BaseModel):
    aid = IntegerField()
    buynum = IntegerField()
    oid = CharField(index=True)
    price = FloatField()
    title = CharField()
    userid = IntegerField(index=True)

    class Meta:
        db_table = 'dede_shops_products'
        primary_key = False

class DedeShopsUserinfo(BaseModel):
    address = CharField()
    consignee = CharField()
    des = CharField()
    email = CharField()
    oid = CharField(index=True)
    tel = CharField()
    userid = IntegerField(index=True)
    zip = IntegerField()

    class Meta:
        db_table = 'dede_shops_userinfo'
        primary_key = False

class DedeSoftconfig(BaseModel):
    argrange = IntegerField()
    dfrank = IntegerField()
    dfywboy = IntegerField()
    downmsg = TextField(null=True)
    downtype = PrimaryKeyField()
    gotojump = IntegerField()
    islocal = IntegerField()
    ismoresite = IntegerField()
    moresitedo = IntegerField()
    sites = TextField(null=True)

    class Meta:
        db_table = 'dede_softconfig'

class DedeSphinx(BaseModel):
    countid = PrimaryKeyField()
    maxaid = IntegerField()

    class Meta:
        db_table = 'dede_sphinx'

class DedeStepselect(BaseModel):
    egroup = CharField(null=True)
    issign = IntegerField(null=True)
    issystem = IntegerField()
    itemname = CharField(null=True)

    class Meta:
        db_table = 'dede_stepselect'

class DedeSysEnum(BaseModel):
    disorder = IntegerField()
    egroup = CharField()
    ename = CharField()
    evalue = CharField()
    issign = IntegerField()

    class Meta:
        db_table = 'dede_sys_enum'

class DedeSysModule(BaseModel):
    hashcode = CharField()
    indexname = CharField()
    indexurl = CharField()
    ismember = IntegerField()
    menustring = TextField(null=True)
    modname = CharField()

    class Meta:
        db_table = 'dede_sys_module'

class DedeSysSet(BaseModel):
    items = TextField(null=True)
    sname = CharField()

    class Meta:
        db_table = 'dede_sys_set'

class DedeSysTask(BaseModel):
    description = CharField()
    dourl = CharField()
    endtime = IntegerField()
    freq = IntegerField()
    islock = IntegerField()
    lastrun = IntegerField()
    parameter = TextField(null=True)
    runtime = CharField(null=True)
    runtype = IntegerField()
    settime = IntegerField()
    sta = CharField(null=True)
    starttime = IntegerField()
    taskname = CharField()

    class Meta:
        db_table = 'dede_sys_task'

class DedeSysconfig(BaseModel):
    aid = IntegerField()
    groupid = IntegerField()
    info = CharField()
    type = CharField()
    value = TextField(null=True)
    varname = CharField(primary_key=True)

    class Meta:
        db_table = 'dede_sysconfig'

class DedeTagindex(BaseModel):
    addtime = IntegerField()
    count = IntegerField()
    monthcc = IntegerField()
    monthup = IntegerField()
    tag = CharField()
    total = IntegerField()
    typeid = IntegerField()
    weekcc = IntegerField()
    weekup = IntegerField()

    class Meta:
        db_table = 'dede_tagindex'

class DedeTaglist(BaseModel):
    aid = IntegerField()
    arcrank = IntegerField()
    tag = CharField()
    tid = IntegerField()
    typeid = IntegerField()

    class Meta:
        db_table = 'dede_taglist'
        indexes = (
            (('tid', 'aid'), True),
        )
        primary_key = CompositeKey('aid', 'tid')

class DedeUploads(BaseModel):
    aid = PrimaryKeyField()
    arcid = IntegerField(index=True)
    filesize = IntegerField()
    height = CharField()
    mediatype = IntegerField()
    mid = IntegerField(index=True)
    playtime = CharField()
    title = CharField()
    uptime = IntegerField()
    url = CharField()
    width = CharField()

    class Meta:
        db_table = 'dede_uploads'

class DedeVerifies(BaseModel):
    cthash = CharField()
    filename = CharField()
    method = CharField()
    nameid = CharField(primary_key=True)

    class Meta:
        db_table = 'dede_verifies'

class DedeVote(BaseModel):
    aid = PrimaryKeyField()
    endtime = IntegerField()
    isallow = IntegerField()
    isenable = IntegerField()
    ismore = IntegerField()
    spec = IntegerField()
    starttime = IntegerField()
    totalcount = IntegerField()
    view = IntegerField()
    votename = CharField()
    votenote = TextField(null=True)

    class Meta:
        db_table = 'dede_vote'

class DedeVoteMember(BaseModel):
    uptime = IntegerField()
    userid = CharField()
    voteid = IntegerField()

    class Meta:
        db_table = 'dede_vote_member'

