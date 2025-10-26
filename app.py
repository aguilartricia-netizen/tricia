<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Student Management</title>

  <!-- ======= Styles ======= -->
  <style>
    :root{
      --bg:#0f1724;
      --card:#0b1220;
      --accent:#7c5cff;
      --muted:#9aa4b2;
      --glass: rgba(255,255,255,0.03);
      --success: #3bd671;
      --danger: #ff6b6b;
      --radius: 12px;
      font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }

    html,body{
      height:100%;
      margin:0;
      background:
        radial-gradient(1200px 600px at 10% 10%, rgba(124,92,255,0.08), transparent 8%),
        linear-gradient(180deg, rgba(10,14,22,1) 0%, rgba(15,23,36,1) 100%);
      color:#e6eef6;
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
    }

    .wrap{
      max-width:1000px;
      margin:40px auto;
      padding:28px;
      display:grid;
      grid-template-columns: 380px 1fr;
      gap:24px;
    }

    .card{
      background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.015));
      border-radius: var(--radius);
      padding:18px;
      box-shadow: 0 6px 30px rgba(2,6,23,0.6);
      border: 1px solid rgba(255,255,255,0.03);
    }

    h1{
      margin:0 0 10px 0;
      font-size:20px;
      letter-spacing:0.2px;
    }
    p.lead{
      margin:0 0 18px 0;
      color:var(--muted);
      font-size:13px;
    }

    form .row{
      display:flex;
      gap:10px;
      margin-bottom:12px;
    }

    label{
      display:block;
      font-size:13px;
      color:var(--muted);
      margin-bottom:6px;
    }

    input[type="text"], select, input[type="number"]{
      width:100%;
      padding:10px 12px;
      border-radius:10px;
      border:1px solid rgba(255,255,255,0.04);
      background:var(--glass);
      color:inherit;
      box-sizing:border-box;
      outline:none;
      transition:box-shadow .15s, transform .08s;
    }
    input:focus, select:focus{
      box-shadow: 0 6px 26px rgba(124,92,255,0.06), 0 1px 0 rgba(124,92,255,0.06) inset;
      transform: translateY(-1px);
    }

    .actions{
      display:flex;
      gap:8px;
      margin-top:6px;
    }
    button{
      padding:10px 14px;
      border-radius:10px;
      border: none;
      cursor:pointer;
      font-weight:600;
      letter-spacing:0.2px;
      box-shadow: 0 6px 18px rgba(2,6,23,0.45);
    }
    .btn-primary{ background: linear-gradient(90deg,var(--accent), #5aa5ff); color:white;}
    .btn-update{ background:var(--success); color:#04220d; }
    .btn-delete{ background:var(--danger); color:white; }
    .btn-ghost{ background:transparent; color:var(--muted); border:1px solid rgba(255,255,255,0.03); }

    /* students list */
    .list-header{
      display:flex;
      justify-content:space-between;
      align-items:center;
      margin-bottom:12px;
    }
    .search{
      display:flex;
      gap:8px;
      align-items:center;
    }
    .list{
      display:grid;
      gap:10px;
      max-height:64vh;
      overflow:auto;
      padding-right:6px;
    }

    .student-item{
      display:flex;
      justify-content:space-between;
      align-items:center;
      padding:10px;
      border-radius:10px;
      background: linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0.005));
      border:1px solid rgba(255,255,255,0.02);
    }
    .student-meta{
      display:flex;
      gap:12px;
      align-items:center;
    }
    .avatar{
      width:44px;
      height:44px;
      border-radius:10px;
      background:linear-gradient(180deg,#2b2f3a,#111424);
      display:flex;
      align-items:center;
      justify-content:center;
      font-weight:700;
      color:var(--accent);
      border:1px solid rgba(255,255,255,0.03);
    }
    .muted{ color:var(--muted); font-size:13px; }

    .small{
      font-size:13px;
      color:var(--muted);
    }

    footer.note{
      margin-top:16px;
      color:var(--muted);
      font-size:13px;
    }

    @media (max-width:880px){
      .wrap{ grid-template-columns: 1fr; padding:16px; gap:14px; }
    }
  </style>
</head>
<body>
  <div class="wrap">
    <!-- Form Card -->
    <div class="card" id="formCard">
      <h1>Student Form</h1>
      <p class="lead">Add, update, or delete a student. Fields are simple for demo purposes.</p>

      <form id="studentForm" autocomplete="off">
        <!-- hidden id for edit -->
        <input type="hidden" id="studentId" />

        <div class="row">
          <div style="flex:1">
            <label for="name">Full name</label>
            <input id="name" type="text" placeholder="e.g. Maria Santos" required />
          </div>
        </div>

        <div class="row">
          <div style="width:120px">
            <label for="grade">Grade</label>
            <input id="grade" type="number" min="1" max="12" placeholder="10" required />
          </div>

          <div style="flex:1">
            <label for="section">Section</label>
            <select id="section">
              <option value="Zechariah">Zechariah</option>
              <option value="Matthew">Matthew</option>
              <option value="Mark">Mark</option>
              <option value="Luke">Luke</option>
              <option value="John">John</option>
            </select>
          </div>
        </div>

        <div class="actions">
          <button class="btn-primary" type="submit" id="saveBtn">Add Student</button>
          <button class="btn-update" type="button" id="updateBtn" style="display:none">Save Changes</button>
          <button class="btn-delete" type="button" id="removeBtn" style="display:none">Delete</button>
          <button class="btn-ghost" type="button" id="clearBtn">Clear</button>
        </div>

        <p class="note muted" style="margin-top:12px">Tip: click a student on the right to load into the form for editing.</p>
      </form>
    </div>

    <!-- List Card -->
    <div class="card" id="listCard">
      <div class="list-header">
        <div>
          <h1 style="font-size:16px; margin:0">Students</h1>
          <p class="small" id="totalCount">Loading…</p>
        </div>
        <div class="search">
          <input id="search" type="text" placeholder="Search name or section" style="padding:8px 10px; border-radius:10px; border:1px solid rgba(255,255,255,0.03); background:var(--glass); color:inherit;" />
        </div>
      </div>

      <div class="list" id="studentsList" aria-live="polite">
        <!-- dynamically filled -->
      </div>

      <footer class="note">This demo uses the REST endpoints at <code>/students</code>. Make sure your Flask API is running.</footer>
    </div>
  </div>

  <!-- ======= JavaScript ======= -->
  <script>
    // API base - change if needed (e.g. http://localhost:5000)
    const API_BASE = '';

    // Elements
    const studentForm = document.getElementById('studentForm');
    const nameInput = document.getElementById('name');
    const gradeInput = document.getElementById('grade');
    const sectionInput = document.getElementById('section');
    const idInput = document.getElementById('studentId');

    const saveBtn = document.getElementById('saveBtn');
    const updateBtn = document.getElementById('updateBtn');
    const removeBtn = document.getElementById('removeBtn');
    const clearBtn = document.getElementById('clearBtn');

    const studentsList = document.getElementById('studentsList');
    const totalCount = document.getElementById('totalCount');
    const search = document.getElementById('search');

    let studentsCache = [];

    // Helper: render student list
    function renderList(filter = '') {
      const q = filter.trim().toLowerCase();
      const visible = studentsCache.filter(s => {
        if (!q) return true;
        return (s.name || '').toLowerCase().includes(q) || (s.section || '').toLowerCase().includes(q) || String(s.grade).includes(q);
      });
      studentsList.innerHTML = '';
      if (visible.length === 0) {
        studentsList.innerHTML = '<div class="muted">No students found.</div>';
      } else {
        visible.forEach(s => {
          const el = document.createElement('div');
          el.className = 'student-item';
          el.innerHTML = `
            <div class="student-meta">
              <div class="avatar">${(s.name || 'U').split(' ').slice(0,2).map(x=>x[0]).join('').toUpperCase()}</div>
              <div>
                <div style="font-weight:600">${escapeHtml(s.name)}</div>
                <div class="muted">${escapeHtml(s.section)} · Grade ${escapeHtml(String(s.grade))}</div>
              </div>
            </div>
            <div style="display:flex; gap:8px; align-items:center;">
              <button class="btn-ghost" data-id="${s.id}" title="Edit">Edit</button>
            </div>
          `;
          // edit when clicking edit button or entire item
          el.querySelector('button').addEventListener('click', () => loadStudentToForm(s));
          el.addEventListener('click', (e) => {
            // avoid double-handling when pressing edit btn
            if (e.target.tagName.toLowerCase() === 'button') return;
            loadStudentToForm(s);
          });
          studentsList.appendChild(el);
        });
      }
      totalCount.textContent = `${visible.length} shown — ${studentsCache.length} total`;
    }

    // Escape utility to avoid injection in text nodes
    function escapeHtml(str){ return String(str).replace(/[&<>"']/g, s => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[s])); }

    // Load students from API
    async function loadStudents(){
      try {
        const res = await fetch(API_BASE + '/students');
        if (!res.ok) throw new Error('Failed to fetch');
        const payload = await res.json();
        // Accept either array or {students: [...]}
        studentsCache = Array.isArray(payload) ? payload : (payload.students || payload);
        renderList(search.value);
      } catch(err){
        studentsList.innerHTML = `<div class="muted">Unable to load students. Make sure the API is running (console: ${escapeHtml(err.message)}).</div>`;
        totalCount.textContent = '0';
      }
    }

    // Add student (POST)
    async function addStudent(data){
      const res = await fetch(API_BASE + '/students', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(data)
      });
      if (!res.ok) {
        const err = await res.json().catch(()=>({message:'Unknown'}));
        throw new Error(err.message || 'Add failed');
      }
      return res.json();
    }

    // Update student (PUT)
    async function updateStudentAPI(id, data){
      const res = await fetch(API_BASE + '/students/' + id, {
        method: 'PUT',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify(data)
      });
      if (!res.ok) {
        const err = await res.json().catch(()=>({message:'Unknown'}));
        throw new Error(err.message || 'Update failed');
      }
      return res.json();
    }

    // Delete student (DELETE)
    async function deleteStudentAPI(id){
      const res = await fetch(API_BASE + '/students/' + id, {
        method: 'DELETE'
      });
      if (!res.ok) {
        const err = await res.json().catch(()=>({message:'Unknown'}));
        throw new Error(err.message || 'Delete failed');
      }
      return res.json();
    }

    // Form submit: Add
    studentForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const payload = {
        name: nameInput.value.trim(),
        grade: Number(gradeInput.value),
        section: sectionInput.value
      };
      try {
        saveBtn.disabled = true;
        await addStudent(payload);
        await loadStudents();
        studentForm.reset();
        idInput.value = '';
        toggleFormMode('add');
        alert('Student added!');
      } catch (err){
        alert('Error: ' + err.message);
      } finally { saveBtn.disabled = false; }
    });

    // Update button handler
    updateBtn.addEventListener('click', async () => {
      const id = idInput.value;
      if (!id) return alert('No student selected.');
      const payload = {
        name: nameInput.value.trim(),
        grade: Number(gradeInput.value),
        section: sectionInput.value
      };
      try {
        updateBtn.disabled = true;
        await updateStudentAPI(id, payload);
        await loadStudents();
        studentForm.reset();
        idInput.value = '';
        toggleFormMode('add');
        alert('Student updated!');
      } catch(err){
        alert('Error: ' + err.message);
      } finally { updateBtn.disabled = false; }
    });

    // Delete button handler
    removeBtn.addEventListener('click', async () => {
      const id = idInput.value;
      if (!id) return alert('No student selected.');
      if (!confirm('Delete this student?')) return;
      try {
        removeBtn.disabled = true;
        await deleteStudentAPI(id);
        await loadStudents();
        studentForm.reset();
        idInput.value = '';
        toggleFormMode('add');
        alert('Student deleted');
      } catch(err){
        alert('Error: ' + err.message);
      } finally { removeBtn.disabled = false; }
    });

    // Clear form
    clearBtn.addEventListener('click', () => {
      studentForm.reset();
      idInput.value = '';
      toggleFormMode('add');
    });

    // Load student into form for edit
    function loadStudentToForm(s){
      idInput.value = s.id;
      nameInput.value = s.name || '';
      gradeInput.value = s.grade || '';
      sectionInput.value = s.section || '';
      toggleFormMode('edit');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Toggle between add vs edit modes
    function toggleFormMode(mode){
      if (mode === 'edit'){
        saveBtn.style.display = 'none';
        updateBtn.style.display = 'inline-block';
        removeBtn.style.display = 'inline-block';
      } else {
        saveBtn.style.display = 'inline-block';
        updateBtn.style.display = 'none';
        removeBtn.style.display = 'none';
      }
    }

    // Live search
    search.addEventListener('input', () => renderList(search.value));

    // Initial load
    loadStudents();
  </script>
</body>
</html>
