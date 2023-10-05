import git

class GitClient:
    def __init__(self, local_repo_path, remote_repo_url):
        self.local_repo_path = local_repo_path
        self.remote_repo_url = remote_repo_url
        self.repo = None

        if not git.repo.fun.is_git_dir(local_repo_path):
            self.repo = git.Repo.init(local_repo_path)
            self.repo.create_remote('origin', remote_repo_url)
        else:
            self.repo = git.Repo(local_repo_path)

    def clone(self):
        if not self.repo : 
            git.Repo.clone_from(self.remote_repo_url, self.local_repo_path)
            self.repo = git.Repo(self.local_repo_path)

    def pull(self):
        self.repo.remotes.origin.pull()

    def push(self):
        self.repo.remotes.origin.push()

    def commit(self, message):
        self.repo.git.add(A=True)
        self.repo.index.commit(message)

if __name__ == "__main__":
    client = GitClient('/home/debian/project', 'git@192.168.1.10:/opt/git/project.git')    
