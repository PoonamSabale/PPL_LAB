import pygtk
import gtk

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()
        self.set_title("College Portal")
        self.set_default_size(400, 500)
        self.set_position(gtk.WIN_POS_CENTER)

        self.label1 = gtk.Label("Name:")
        self.entry1 = gtk.Entry()
        self.label2 = gtk.Label("MIS:")
        self.entry2 = gtk.Entry()
        self.label3 = gtk.Label("Branch:")
        self.entry3 = gtk.Entry()
        self.label4 = gtk.Label("Year:")
        self.entry4 = gtk.Entry()


        self.btn = gtk.Button("SUBMIT")
        self.btn.connect("clicked", self.finish)

        fixed = gtk.Fixed()
        fixed.put(self.label1, 100, 100)
        fixed.put(self.entry1, 100, 120)
        fixed.put(self.label2, 100, 150)
        fixed.put(self.entry2, 100, 170)
        fixed.put(self.label3, 100, 200)
        fixed.put(self.entry3, 100, 220)
        fixed.put(self.label4, 100, 250)
        fixed.put(self.entry4, 100, 270)
        fixed.put(self.btn, 100, 300)

        self.add(fixed)
        self.show_all()

    def finish(self, widget):
        print 'Form submitted successfully'
        print'details are :\n1.Name:', self.entry1.get_text(),'\n2.Mis:',self.entry2.get_text(),'\n3.Branch:',self.entry3.get_text(),'\n4.Year:',self.entry4.get_text()

PyApp()
gtk.main()
